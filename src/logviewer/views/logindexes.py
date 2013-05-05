import pyes
import indexes
'''
    Creates indexes in elasticsearch

    @package logviewer.views.logindexes
    @authors Deniz Eren
    @authors Ibrahim Ercan
    @authors Ersan Vural Zorlu
    @authors Nijad Ahmadli    
    @copyright This project is released under BSD license
    @date 2013/03/31
'''

ES_SERVER = '127.0.0.1:9200'
LOG_TYPES = [log_t for log_t in dir(indexes) if not log_t.startswith('__')]


def create_mappings():
    '''
        Creates mappings according to indexes
    '''

    # Connect to elasticsearch
    conn = pyes.ES(ES_SERVER)

    # Create mappings
    for log_t in LOG_TYPES:
        mapping = eval('indexes.'+log_t)
        conn.put_mapping(log_t, {'properties':mapping}, 'logviewer')


def main():
    '''
        Main function
    '''
    create_mappings()


if __name__ == '__main__':
    main()
