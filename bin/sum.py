#!/usr/bin/python
"""usage: sum"""
import sys

if __name__ == '__main__':
    total = sum(map(int, sys.stdin.readlines()))
    print total
