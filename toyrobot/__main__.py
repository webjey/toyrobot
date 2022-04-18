import sys
import os
from pathlib import Path

from toyrobot.grid import Grid
from toyrobot.controller import Controller



if __name__ == '__main__':

    grid = Grid(cols=5, rows=5)
    controller = Controller(grid)

    print(f'Valid commands are: ', ', '.join(controller.commands))

    while (True):
        user_input = input()
        if not user_input:
            continue

        controller.process_command(user_input)

