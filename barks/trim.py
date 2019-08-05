#!/usr/bin/python
"""usage: selector <CSS selector (.btn etc.)>

accepts html through stdin"""
import getopt
import sys

from bs4 import BeautifulSoup


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
        inf = sys.stdin
    except getopt.GetoptError:
        print __doc__
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print __doc__
            sys.exit()
    print inf.read().strip()
