#!/usr/bin/env python3
"""
#for getting file input

import fileinput
with fileinput.input() as f_input:
    for line in f_input:
        print(line)

"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help='increase verbosity')
parser.parse_args()
