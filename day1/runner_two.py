#!/usr/bin/env python3
import argparse
from frequency_parser import (
    get_input_file_as_argument, FrequencyCalibrator
)


CLI_DESCRIPTION = 'Process second Advent of Code puzzle for the Day 1.'


def main():
    input_file = get_input_file_as_argument(CLI_DESCRIPTION)
    calibrator = FrequencyCalibrator(input_file)
    duplicate_frequency = calibrator.calibrate_until_duplicate_frequencies_received()
    print(duplicate_frequency)


if __name__ == '__main__':
    main()
