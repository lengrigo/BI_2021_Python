#!/usr/bin/env python3

import sys

lst = []
if not sys.stdin.isatty():
    for line in sys.stdin:
        lst.append(line)
else:
    input_file = sys.argv[1]
    with open(input_file, mode="r") as file:
        lst = file.readlines()

print(*sorted(lst), sep='', end='')
