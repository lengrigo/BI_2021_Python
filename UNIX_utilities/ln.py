#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--symbolic', help='make symbolic link', action='store_true')
parser.add_argument('target', nargs='?', type=str)
parser.add_argument('link_name', nargs='?', type=str)
args = parser.parse_args()

if args.symbolic:
    os.symlink(src=args.target, dst=args.link_name)
else:
    os.link(src=args.target, dst=args.link_name)
