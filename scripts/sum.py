#!/usr/bin/python
"""usage: cat file_with_numbers.txt | sum"""
import sys

if __name__ == '__main__':
    total = sum(map(int, sys.stdin.readlines()))
    print(total)
