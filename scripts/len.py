#!/usr/bin/python
"""usage: cat lines | len"""
import sys

if __name__ == '__main__':
    try:
        for line in sys.stdin.readlines():
            print(len(line))
    except IOError:  # problem in bash?
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
