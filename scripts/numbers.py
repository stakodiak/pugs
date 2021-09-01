#!/usr/bin/python3
"""
$ thousands 600000000000.0
600,000,000,000.00

Adds commas to thousands places of given number.
"""
import sys

if __name__ == '__main__':
    try:
        inf = [sys.argv[1]]
    except IndexError:
        inf = sys.stdin.readlines()
    for line in inf:
        print("{:,.2f}".format(float(line)))
