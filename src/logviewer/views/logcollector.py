import metadata
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
    @copyright This project is released under BSD license
    @date 2013/03/31
'''

LOGVIEWER_INDEX='logviewer'
LOGVIEWER_SERVER='127.0.0.1:9500'

class LogCollector(object):
    '''
        Inserts logs to elasticsearch
    '''

    def __init__(self):
        '''
            Sets metadata object.
        '''
        self.metadata = metadata.MetaData()

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

    def write_to_database(self, log_type, log_line):
        '''
            Writes logline to DB by its type.
    
            @param log_type String: Type of log stream.
            @param log_line String: Log line from stream.
        '''
        # Combine filter options with log line
        # Ex:
        #   {'logdate':'2012-12-12 12:12:12', 'logtext':'this is log'}
        splitted_line = log_line.strip().split(self.metadata_dict[log_type]['delimiter'].replace("'",""))
        log_to_insert = dict(zip(
                self.metadata_dict[log_type]['filter_columns'], 
                splitted_line
               ))

        # Connect to elasticsearch
        conn = pyes.ES(LOGVIEWER_SERVER)

        # Write data to elasticseach
        conn.index(log_to_insert, LOGVIEWER_INDEX, log_type)

def parse_args(log_types):
    '''
        Parses command line arguments

        @param log_types List: Possible log types.
        @returns HTTP response which includes log data in JSON format.
    '''
    parser = OptionParser()
    parser.add_option("-t", "--type",
                      action="store",
                      dest="type",
                      choices=log_types,
                      help="log stream type")

    (options, args) = parser.parse_args()

    if not options.type:
        print 'You must specify a log type.'
        sys.exit(1)

    return options

def main():
    '''
        Main function which writes log to database
    '''
    collector = LogCollector()
    collector.read_meta_data()

    # Parse Args
    options = parse_args(collector.log_types)

    # Get log line from stdin
    log_line = sys.stdin.readline()

    # Write log to database
    collector.write_to_database(options.type, log_line)

if __name__ == '__main__':
    main()
