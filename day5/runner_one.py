#!/usr/bin/env python3
import argparse


CLI_DESCRIPTION = 'Process first Advent of Code puzzle for the Day 5.'


def get_input_file_as_argument(cli_description):
    parser = argparse.ArgumentParser(description=cli_description)
    parser.add_argument('file', nargs=1, type=argparse.FileType('r'))
    parsed_arguments = parser.parse_args()
    return parsed_arguments.file[0]


def case_test(character_one, character_two):
    return character_one != character_two and character_one.lower() == character_two.lower()


def react_polymer(input_string):
    i = 1
    while True:
        character_one = input_string[i]
        character_two = input_string[i-1]
        if case_test(character_one, character_two):
            i -= 1
            del input_string[i]
            del input_string[i]
            if i == 0:
                i = 1
        else:
            i += 1

        if i + 1 > len(input_string):
            break
    return input_string


def main():
    input_file = get_input_file_as_argument(CLI_DESCRIPTION)
    input_string = list(input_file.read())
    result = react_polymer(input_string)
    print(len(input_string) - 1)

if __name__ == '__main__':
    main()
