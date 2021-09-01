#!/usr/bin/python
"""usage: `cat text | endswith string`"""
import sys

if __name__ == '__main__':
    try:
        # Print all lines whose contents end with given arg
        key = sys.argv[1]
        for line in sys.stdin.readlines():
            if line.rstrip().endswith(key):
                sys.stdout.write(line)
    except IndexError:
        print(__doc__)
        sys.exit(0)
    except IOError:
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
