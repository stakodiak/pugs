#!/usr/bin/python3
"""usage: cat text | rot13"""
import sys

if __name__ == '__main__':
    try:
        for line in sys.stdin.readlines():
            sys.stdout.write(line.encode('rot13'))
    except IOError:  # problem in bash?
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
