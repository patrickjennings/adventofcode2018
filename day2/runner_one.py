#!/usr/bin/env python3
import argparse
from collections import Counter


CLI_DESCRIPTION = 'Process first Advent of Code puzzle for the Day 2.'


def get_input_file_as_argument(cli_description):
    parser = argparse.ArgumentParser(description=cli_description)
    parser.add_argument('file', nargs=1, type=argparse.FileType('r'))
    parsed_arguments = parser.parse_args()
    return parsed_arguments.file[0]


def check_for_duplicates_and_triplicates(input_string):
    character_counts = Counter(input_string).values()
    return (2 in character_counts, 3 in character_counts)


def hash_input_file(input_file):
    character_counts = (
        check_for_duplicates_and_triplicates(input_string)
        for input_string in input_file
    )
    doubles, triples = 0, 0
    for character_count in character_counts:
        doubles += character_count[0]
        triples += character_count[1]
    return doubles * triples


def main():
    input_file = get_input_file_as_argument(CLI_DESCRIPTION)
    input_file_hash = hash_input_file(input_file)
    print(input_file_hash)


if __name__ == '__main__':
    main()
