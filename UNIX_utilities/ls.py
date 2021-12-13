#!/usr/bin/env python3

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--all', help='do not ignore entries starting with .', action='store_true')
parser.add_argument('directory', nargs='*', default='.', type=str)

args = parser.parse_args()
dirs = args.directory
if args.all:
    if len(dirs) == 1:
        print(*sorted(os.listdir(dirs[0])), sep='\n')
    else:
        for direct in dirs:
            print(direct, ':', sep='')
            print(*sorted(os.listdir(direct)), sep='\n')
else:
    output = []
    if len(dirs) == 1:
        for i in os.listdir(dirs[0]):
            if i[0] != '.':
                output.append(i)
        print(*sorted(output), sep='\n')
    else:
        for direct in dirs:
            print(direct, ':', sep='')
            output = []
            for i in os.listdir(direct):
                if i[0] != '.':
                    output.append(i)
            print(*sorted(output), sep='\n')
