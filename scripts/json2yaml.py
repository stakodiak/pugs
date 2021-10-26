#!/usr/local/bin/python3
"""convert YAML to JSON via stdin"""
import sys
import yaml
import json

def main():
    try:
        inf = open(sys.argv[1], 'r') 
    except IndexError:
        inf = sys.stdin
    data = json.loads(inf.read())
    print(yaml.dump(yaml.load(json.dumps(data, indent=2)), default_flow_style=False))

if __name__ == '__main__':
    main()
