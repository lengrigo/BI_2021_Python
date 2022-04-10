#!/usr/bin/env python3

import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-r', '-R', '--recursive', help='removes directories recursively', action='store_true')
parser.add_argument('path', nargs='*', type=str)
args = parser.parse_args()

paths = args.path
for i in paths:
    if args.recursive and os.path.isdir(i):
        shutil.rmtree(i)
    elif not args.recursive and os.path.isdir(i):
        print(f'can not remove {i}: Is a directory')
    elif not args.recursive and os.path.isfile(i):
        os.remove(i)
