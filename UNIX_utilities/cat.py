#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='*', type=str)
args = parser.parse_args()

for file in args.file:
    with open(file, mode="r") as f:
        for line in f.readlines():
            print(line, end='')
