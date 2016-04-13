"""
Print range of lines.

usage:
    range 4

output:
    1
    2
    3
    4
"""
def execute(inf):
    import sys
    num_lines = int(inf.read().strip())
    for i in xrange(1, num_lines + 1):
        sys.stdout.write(str(i) + '\n')

if __name__ == '__main__':
    inf = sys.stdin
    if len(sys.argv) > 1:
        inf = sys.argv[1]
    execute(inf)
