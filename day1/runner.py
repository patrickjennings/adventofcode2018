#!/usr/bin/env python3
import argparse
from frequency_parser import (
    get_input_file_as_argument, input_frequency_generator, sum_input_frequencies
)


CLI_DESCRIPTION = 'Process first Advent of Code input for the Day 1 puzzle.'


def main():
    input_file = get_input_file_as_argument(CLI_DESCRIPTION)
    result = sum_input_frequencies(input_file)
    print(result)

if __name__ == '__main__':
    main()
