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
        print(__doc__)
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(__doc__)
            sys.exit()
    try:
        soup = BeautifulSoup(inf, "html.parser")
        for selector in args:
            for e in soup.select(selector):
                if len(e) > 1:
                    print(e)
                else:
                    print(e.get_text())
    except IndexError:
        print(__doc__)
        sys.exit(1)
