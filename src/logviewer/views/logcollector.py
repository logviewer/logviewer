import metadata
import multiprocessing
import socket
import re
import sys
import pyes
from optparse import OptionParser
'''
    Log collecting module.

    Gets logs from stream and puts them into elasticsearch.

    @package logviewer.views.logcollector
    @authors Deniz Eren
    @authors Ibrahim Ercan
    @authors Ersan Vural Zorlu
    @authors Nijad Ahmadli    
    @authors http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/
    @copyright This project is released under BSD license
    @date 2013/03/31
'''

LOGVIEWER_INDEX='logviewer'
LOGVIEWER_SERVER='127.0.0.1:9500'

import sys, os, time, atexit
from signal import SIGTERM 

class LogDaemon(object):
    '''
    A generic daemon class.
    
    Usage: subclass the Daemon class and override the run() method

    Source: http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/
    '''
    def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile
        self.log_processes = []
    
    def daemonize(self):
        '''
        do the UNIX double-fork magic, see Stevens' 'Advanced 
        Programming in the UNIX Environment' for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        '''
        try: 
            pid = os.fork() 
            if pid > 0:
                # exit first parent
                sys.exit(0) 
        except OSError, e: 
            sys.stderr.write('fork #1 failed: %d (%s)\n' % (e.errno, e.strerror))
            sys.exit(1)
    
        # decouple from parent environment
        os.chdir('/') 
        os.setsid() 
        os.umask(0) 
    
        # do second fork
        try: 
            pid = os.fork() 
            if pid > 0:
                # exit from second parent
                sys.exit(0) 
        except OSError, e: 
            sys.stderr.write('fork #2 failed: %d (%s)\n' % (e.errno, e.strerror))
            sys.exit(1) 
    
        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
    
        # write pidfile
        atexit.register(self.delpid)
        pid = str(os.getpid())
        file(self.pidfile,'w+').write('%s\n' % pid)
    
    def delpid(self):
        os.remove(self.pidfile)

    def start(self):
        '''
        Start the daemon
        '''
        # Check for a pidfile to see if the daemon already runs
        try:
            pf = file(self.pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
    
        if pid:
            message = 'pidfile %s already exist. Daemon already running?\n'
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)
        
        # Start the daemon
        self.daemonize()
        self.run()

    def stop(self):
        '''
        Stop the daemon
        '''
        # Get the pid from the pidfile
        try:
            pf = file(self.pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
    
        if not pid:
            message = 'pidfile %s does not exist. Daemon not running?\n'
            sys.stderr.write(message % self.pidfile)
            return # not an error in a restart

        # Try killing the daemon process    
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError, err:
            err = str(err)
            if err.find('No such process') > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print str(err)
                sys.exit(1)
        finally:
            for log_p in self.log_processes:
                log_p.shutdown()

    def restart(self):
        '''
        Restart the daemon
        '''
        self.stop()
        self.start()

    def get_log_types(self):
        '''
            Gets available log types
        '''
        mdata = metadata.MetaData()
        metadata_dict = mdata.read_ini_file()
        self.log_types = metadata_dict.keys()

    def run(self):
        '''
        '''
        self.get_log_types()

        for log_t in self.log_types:
            collector = LogCollector(log_t)
            self.log_processes.append(collector)
            collector.start()


class LogCollector(multiprocessing.Process):
    '''
        Inserts logs to elasticsearch
    '''

    def __init__(self, log_type):
        '''
            Sets metadata object.
        '''
        multiprocessing.Process.__init__(self)
        self.exit = multiprocessing.Event()
        self.metadata = metadata.MetaData()
        self.log_type = log_type
        self.socketfile = '/var/log/' + log_type + '.sock'

    def read_meta_data(self):
        '''
            Reads metadata dictionary.

            Metadata dictionary:
            {
             'network': {
                         'filter_columns': ['Month', 'Day', 'Time'], 
                         'delimiter': "' '"
                        }
            }
        '''
        self.metadata_dict = self.metadata.read_ini_file()
 
        # Get log types in metadata
        self.log_types = self.metadata_dict.keys()

    def connect_socket(self):
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.bind(self.socketfile)
        s.listen(1)
        conn, addr = s.accept()

        return conn, addr

    def reformat_log(self, log_type, log_line):
        if log_type == 'network':
            log_line = re.sub(' [a-zA-Z0-9]+=', ' ', log_line)
            log_line = re.sub(' \[[ ]*[0-9]+\.[0-9]+\] ', ' ', log_line)
        elif log_type == 'sshd':
            log_line = re.sub('([0-9]+) (Accepted|Failed) (password) for ([^ ]+) from ([^ ]+) port ([0-9]+)', r'\1 \2-\3 \4 \5 \6', log_line)

        return log_line

    def write_to_database(self, log_type, log_line):
        '''
            Writes logline to DB by its type.
    
            @param log_type String: Type of log stream.
            @param log_line String: Log line from stream.
        '''
        # Combine filter options with log line
        # Ex:
        #   {'logdate':'2012-12-12 12:12:12', 'logtext':'this is log'}
        log_line = self.reformat_log(log_type, log_line)
        
        splitted_line = log_line.strip().split(self.metadata_dict[log_type]['delimiter'].replace("'",""))
        log_to_insert = dict(zip(
                self.metadata_dict[log_type]['filter_columns'], 
                splitted_line
               ))

        # Connect to elasticsearch
        conn = pyes.ES(LOGVIEWER_SERVER)

        # Write data to elasticseach
        conn.index(log_to_insert, LOGVIEWER_INDEX, log_type)

    def run(self):
        self.read_meta_data()

        conn, addr = self.connect_socket()
        while not self.exit.is_set():
            log_line = conn.recv(1024)
            if not log_line: continue
            self.write_to_database(self.log_type, log_line)

        conn.close()
        os.remove(self.socketfile)

    def shutdown(self):
        self.exit.set()


def main():
    '''
        Main function which writes log to database
    '''
    daemon = LogDaemon('/var/run/log-collector.pid')

    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)

if __name__ == '__main__':
    main()
