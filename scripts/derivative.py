#!/usr/bin/python
"""usage: derivative < `cat my-sequence.txt`

Computes the derivative of a given sequence of integers.
"""
import sys

if __name__ == '__main__':
    try:
        inf = open(sys.argv[1], 'r')
    except IndexError:
        inf = sys.stdin.readlines()
    seq = map(float, inf)
    for a, b in zip(seq, seq[1:]):
        print(b - a)
