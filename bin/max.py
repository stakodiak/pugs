#!/usr/bin/python
"""usage: max [file]"""
import sys

if __name__ == '__main__':
    try:
        inf = open(sys.argv[1], 'r')
    except IndexError:
        inf = sys.stdin.readlines()
    print max(map(int, inf))
