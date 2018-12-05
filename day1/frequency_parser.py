import argparse
from itertools import cycle


def get_input_file_as_argument(cli_description):
    parser = argparse.ArgumentParser(description=cli_description)
    parser.add_argument('file', nargs=1, type=argparse.FileType('r'))
    parsed_arguments = parser.parse_args()
    return parsed_arguments.file[0]


def sum_input_frequencies(input_file):
    generator = input_frequency_generator(input_file)
    return sum(generator)


def input_frequency_generator(input_file):
    for next_input in input_file:
        yield int(next_input)


class FrequencyCalibrator:
    def __init__(self, input_file):
        self._input_file = input_file

    def _generate_continuous_frequency_changes(self):
        frequency_generator = input_frequency_generator(self._input_file)
        yield from cycle(frequency_generator)

    def calibrate_until_duplicate_frequencies_received(self):
        frequencies_seen = set()
        frequency_result = 0
        frequency_generator = self._generate_continuous_frequency_changes()

        for next_change in frequency_generator:
            frequency_result += next_change

            if frequency_result in frequencies_seen:
                return frequency_result

            frequencies_seen.add(frequency_result)
