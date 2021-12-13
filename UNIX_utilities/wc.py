#!/usr/bin/env python3

import sys
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--lines', help='print the newline counts', action='store_true')
parser.add_argument('-w', '--words', help='print the word counts', action='store_true')
parser.add_argument('-c', '--bytes', help='print the byte counts', action='store_true')
parser.add_argument('file', nargs='*', type=str)
args = parser.parse_args()


# function for counting what is needed
def counter(lst):
    # counter
    lines = len(lst)
    byt = 0
    words = 0
    reg_words = re.compile(r'\b\w+\b')
    for i in lst:
        for j in reg_words.finditer(i):
            words += 1
        byt += len(i)
    return [lines, words, byt]


# according to argument prints the number
def printer(count_list):
    # -l
    if args.lines:
        print(count_list[0])
    # -c
    elif args.bytes:
        print(count_list[1])
    # -w
    elif args.words:
        print(count_list[2])
    else:
        print(*count_list, sep='\t')
    return


# parsing file
lst = []
if not sys.stdin.isatty():
    for line in sys.stdin:
        lst.append(line)
    printer(counter(lst))
else:
    for file in args.file:
        input_file = file
        with open(input_file, mode="r") as f:
            lst = f.readlines()
            printer(counter(lst))
