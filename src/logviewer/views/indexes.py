'''
    File that keeps log types and their column information

    @package logviewer.views.indexes
    @authors Deniz Eren
    @authors Ibrahim Ercan
    @authors Ersan Vural Zorlu
    @authors Nijad Ahmadli
    @copyright This project is released under BSD license
    @date 2013/03/31
'''

# Network Log
network = {
        u'logdate': {
            'boost': 1.0,
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'long',
            },
        u'service': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            },
        u'rule_num': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            },
        u'action': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            "term_vector" : "with_positions_offsets"
            },
        u'int_iface': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            "term_vector" : "with_positions_offsets"
            },
        u'ext_iface': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            "term_vector" : "with_positions_offsets"
            },
        u'src_ip': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            "term_vector" : "with_positions_offsets"
            },
        u'dst_ip': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            "term_vector" : "with_positions_offsets"
            },
        u'src_port': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            "term_vector" : "with_positions_offsets"
            },
        u'dst_port': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            "term_vector" : "with_positions_offsets"
            },
        u'pkt_len': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'integer',
            },
        u'pkt_tos': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            },
        u'pkt_prec': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            },
        u'pkt_ttl': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'integer',
            },
        u'pkt_id': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'integer',
            },
        u'proto': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            "term_vector" : "with_positions_offsets"
            },
        u'window_size': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'integer',
            },
        u'res': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            },
        u'flags': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            "term_vector" : "with_positions_offsets"
            }
        }

# SSHD Log
sshd = {
        u'logdate': {
            'boost': 1.0,
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'long',
            },
        u'action': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            "term_vector" : "with_positions_offsets"
            },
        u'user': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            "term_vector" : "with_positions_offsets"
            },
        u'ip': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            "term_vector" : "with_positions_offsets"
            },
        u'port': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            "term_vector" : "with_positions_offsets"
            },
        u'ssh': {
            'index': 'not_analyzed',
            'store': 'yes',
            'type': u'string',
            }
        }
