#!/usr/bin/python

'''
    sshd log filtering and parsing script.

    @package logviewer.input_filters.sshd
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

log_line = re.sub('([0-9]+) (Accepted|Failed) (password) for ([^ ]+) from ([^ ]+) port ([0-9]+)', r'\1 \2-\3 \4 \5 \6', log_line)

print log_line
