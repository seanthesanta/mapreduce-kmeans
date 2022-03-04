#!/usr/bin/env python

import sys

#import fileinput
#for line in fileinput.input('in'):
for line in sys.stdin:
    dataline = line.strip().split()
    for c in dataline:
        print '%s' % (c),
    print ''

