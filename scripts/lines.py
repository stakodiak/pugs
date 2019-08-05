#!/usr/bin/python
"""
usage:
    cat my_file.txt | lines range
"""
import sys
from datetime import datetime

if __name__ == '__main__':
    try:
        count = 0
        start = int(sys.argv[1])
        inf = sys.stdin.readlines()
        if len(sys.argv) == 1: # only pulling one line
            end = start
        if len(sys.argv) == 2:  # adding extra line or filename
            try:
                end = int(sys.argv[2])  # user only pulling one line
            except ValueError:  # second arg is filename
                inf = open(sys.argv[2], 'r')
                end = start  # use the same index as above
        elif len(sys.argv) == 2:  # adding extra line or filename
            try:
                end = int(sys.argv[2])  # user only pulling one line
            except ValueError:  # second arg is filename
                inf = open(sys.argv[2], 'r')
                end = start  # use the same index as above
        for line in inf:
            count += 1
            if start <= count <= end:
                sys.stdout.write(line)
    except IOError:  # problem in bash?
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
