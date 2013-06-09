#!/opt/python/bin/python
import ConfigParser
import json
'''
    Reads metadata ini file and returns it as JSON.

    @package logviewer.views.metadata
    @authors Deniz Eren
    @authors Ibrahim Ercan
    @authors Ersan Vural Zorlu
    @authors Nijad Ahmadli
    @copyright This project is released under BSD license
    @date 2013/03/31
'''

METADATA_FILE='/opt/logviewer/src/logviewer/model/metadata.ini'

class MetaData(object):
    '''
        Reads ini and conf files
    '''

    def __init__(self):
        '''
            Sets metadata_file
        '''
        self.metadata_file = METADATA_FILE

    def read_ini_file(self):
        '''
            Reads ini file and returns it as JSON.

            Example output:
            {
             'network': 
                {
                 'filter_columns': ['Month', 'Day', 'Time'], 
                 'delimiter': "' '"
                }
             'servicelist': 
                {
                 'servicelist': ['kernel', 'webfilter', 'ids']
                }
            }

            @returns ini file as JSON file
        '''
        metadata_parser = ConfigParser.ConfigParser()
        metadata_parser.read(self.metadata_file)

        type_filter_list = {}

        for section in metadata_parser.sections():
            type_filter_list[section] = dict(metadata_parser.items(section))
            if section == 'servicelist':
                type_filter_list[section]['servicelist'] = type_filter_list[section]['servicelist'].split(',')
            else:
                type_filter_list[section]['filter_columns'] = type_filter_list[section]['filter_columns'].split(',')

        return type_filter_list

    def write_ini_file(self, log_type, log_dict):
        '''
            Writes ini file
        '''
        metadata_parser = ConfigParser.ConfigParser()
        metadata_parser.read(self.metadata_file)

        try:
            for k in log_dict.keys():
                metadata_parser.set(log_type, k, log_dict[k])

            with open(self.metadata_file, 'w') as f:
                metadata_parser.write(f)
        except Exception as err:
            with open('/tmp/aaa', 'w') as f:
                f.write('\n')
                f.write(str(err))
            return False

        return True


def main():
    '''
        Prints ini file in json format to stdout
    '''
    m = MetaData()
    print json.dumps(m.read_ini_file(), indent=4)

if __name__ == '__main__':
    main()
