import argparse


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
