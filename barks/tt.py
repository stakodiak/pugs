#!/usr/bin/python
"""tt.py - transpose times by hours

usage:
    cat datetimes | tt -4
"""
import datetime
import sys

distance = int(sys.argv[1])
delta = datetime.timedelta(hours=distance)
for line in sys.stdin.readlines():
    time = datetime.datetime.strptime(line.strip(), '%Y-%m-%d %H:%M:%S')
    print time + delta
