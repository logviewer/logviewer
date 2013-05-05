#!/usr/bin/python

'''
    iptables log filtering and parsing script

    @package logviewer.input_filters.iptables
    @authors Deniz Eren
    @authors Ibrahim Ercan
    @authors Ersan Vural Zorlu
    @authors Nijad Ahmadli
    @copyright This project is released under BSD license
    @date 2013/03/31
'''

import re
import sys

log_line = sys.stdin.readline()

# Delete IP=,PROTO= like values
log_line = re.sub(' [a-zA-Z0-9]+=', ' ', log_line)
# Delete unnecessary id [1231312.1331213]
log_line = re.sub(' \[[ ]*[0-9]+\.[0-9]+\] ', ' ', log_line)

print log_line
