#!/usr/bin/env python

import sys

from list_sort import ListSort

usage = """
Usage: ./listSorting.py INPUT_FILE_PATH OUTPUT_FILE_PATH

Example:
    ./listSorting.py ./data/input.txt output.txt

"""

if __name__ == '__main__':
    path_to_input = sys.argv[1]
    path_to_output = sys.argv[2]

    try:
        input_list = open(path_to_input).read()
    except FileNotFoundError:
        print('Invalid input path: %s' % path_to_input)
        print(usage)
        exit(1)

    try:
        output_file = open(path_to_output, 'w+')
    except FileNotFoundError:
        print('Invalid output path: %s' % path_to_output)
        print(usage)
        exit(1)

    sorted = ListSort(input_list).zip_sorted()
    output_file.write(sorted)
