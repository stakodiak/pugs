#!/usr/bin/python
"""usage: echo 1437323391 | u2d"""
import sys
from datetime import datetime

if __name__ == '__main__':
    try:
        for line in sys.stdin.readlines():
            timestamp = float(line)
            print datetime.fromtimestamp(timestamp)
    except IOError:  # problem in bash?
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
