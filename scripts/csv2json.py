#!/usr/bin/python
"""unfortunately named CSV processer with AWK-like syntax"""
import csv
import json
import sys


def main():
    try:
        inf = open(sys.argv[1], 'r') 
    except IndexError:
        inf = sys.stdin
    reader = csv.DictReader(inf)
    rows = [row for row in reader]
    print(json.dumps(rows, indent=2))


if __name__ == '__main__':
    main()
