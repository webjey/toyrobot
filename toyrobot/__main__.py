import sys
import os
import argparse

from toyrobot.grid import Grid
from toyrobot.controller import Controller


def check_positive(value):
    error_msg = f'{value} is an invalid positive integer'

    try:
        value = int(value)
    except:
        raise argparse.ArgumentTypeError(error_msg)

    if value<0:
        raise argparse.ArgumentTypeError(error_msg)

    return value

def is_valid_file(arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')

def parse_args(args):
    parser = argparse.ArgumentParser(description='Toyrobot')
    parser.add_argument('-f', '--file', 
                        required = True,
                        default = 'tests/data/test1.txt',
                        type = is_valid_file,
                        help = (f'Path of file relative to current directory. '
                                f'Contains list of robot commands to execute. '
                                f'1 command per line. Required.'))

    parser.add_argument('-c', '--columns', 
                        default = 5,
                        type = check_positive,
                        help = 'Max number of columns of a grid (or table top). Default value is 5. ')

    parser.add_argument('-r', '--rows', 
                        default = 5,
                        type = check_positive,
                        help = 'Max number of rows of a grid (or table top). Default value is 5.')

    return parser.parse_args(args)

def main():
    args = parse_args(sys.argv[1:])
    grid = Grid(cols=args.columns, rows=args.rows)
    controller = Controller(grid)

    for cmd in args.file:
        controller.process_command(cmd.strip())


if __name__ == '__main__':
    main()
