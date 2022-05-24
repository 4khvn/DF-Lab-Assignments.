#!/usr/bin/python -tt
import argparse
import os
import re
parser = argparse.ArgumentParser()
parser.add_argument('directory',help='path of directory')
parser.add_argument('rule',help='path of rule file')
args = parser.parse_args()
v = open(args.rule,'r').read()
dir = args.directory
rule = re.compile(v)
for root, dirs, files in os.walk(dir):
    for filename in files:
        f = os.path.join(root, filename)
        if os.path.isfile(f):
                a = open(f,'r').read()
                rule.search(a)
                if rule.search(a):
                    print(f, "matched")
                else:
                     print(f, "Not matched")
