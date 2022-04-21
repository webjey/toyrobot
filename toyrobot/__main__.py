import sys
import os
import argparse

from toyrobot.grid import Grid
from toyrobot.controller import Controller


def parse_args(args):

    def positive_number(value):
        error_msg = f'{value} is an invalid positive integer'

        try:
            value = int(value)
        except:
            raise argparse.ArgumentTypeError(error_msg)

        if value<0:
            raise argparse.ArgumentTypeError(error_msg)

        return value

    def file(value):

        if not os.path.exists(value):
            raise argparse.ArgumentTypeError(f'The file {value} does not exist!')

        return value

    parser = argparse.ArgumentParser(description='Toyrobot')

    parser.add_argument('-f', '--file', 
                        required = True,
                        default = 'tests/data/test1.txt',
                        type = file,
                        help = (f'Path of file relative to current directory. '
                                f'Contains list of robot commands to execute. '
                                f'1 command per line. Required.'))

    parser.add_argument('-c', '--columns', 
                        default = 5,
                        type = positive_number,
                        help = 'Max number of columns of a grid (or table top). Default value is 5. ')

    parser.add_argument('-r', '--rows', 
                        default = 5,
                        type = positive_number,
                        help = 'Max number of rows of a grid (or table top). Default value is 5.')

    return parser.parse_args(args)

def main(args):
    parsed = parse_args(args)
    grid = Grid(cols=parsed.columns, rows=parsed.rows)
    controller = Controller(grid)

    with open(parsed.file, 'r') as file:
        for line in file:
            controller.process_command(line.strip())


if __name__ == '__main__':
    main(sys.argv[1:])
