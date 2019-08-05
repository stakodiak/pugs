#!/usr/bin/python
"""usage: `cat text | startswith string`"""
import sys

if __name__ == '__main__':
    try:
        key = sys.argv[1]
        for line in sys.stdin.readlines():
            if line.startswith(key):
                sys.stdout.write(line)
    except IndexError:
        print __doc__
        sys.exit(0)
    except IOError:
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
