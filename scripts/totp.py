#!/usr/local/bin/python3
"""usage: totp <2fa token>"""
import sys
import pyotp

if __name__ == '__main__':
    try:
        inf = [sys.argv[1]]
    except IndexError:
        inf = sys.stdin.readlines()
    try:
        for line in inf:
            print(pyotp.TOTP(line.strip()).now())
    except IOError:  # problem in bash?
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
