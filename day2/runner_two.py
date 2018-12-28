#!/usr/bin/env python3
import argparse
from itertools import combinations


CLI_DESCRIPTION = 'Process second Advent of Code puzzle for the Day 2.'


def get_input_file_as_argument(cli_description):
    parser = argparse.ArgumentParser(description=cli_description)
    parser.add_argument('file', nargs=1, type=argparse.FileType('r'))
    parsed_arguments = parser.parse_args()
    return parsed_arguments.file[0]


def string_compare(first_string, second_string):
    similarities = []
    for first_character, second_character in zip(first_string, second_string):
        if first_character == second_character:
            similarities.append(first_character)
    return similarities


def main():
    input_file = get_input_file_as_argument(CLI_DESCRIPTION)
    string_combinations = combinations(input_file, 2)
    for string_combination in string_combinations:
        string_one = string_combination[0]
        string_two = string_combination[1]
        similarities = string_compare(string_one, string_two)
        if len(string_one) - len(similarities) == 1:
            print(''.join(similarities))

if __name__ == '__main__':
    main()
