import logging
import operator
from toyrobot.orientation import Orientation


class Robot():
    """
    A class for simulating a robot

    Attributes:
    x (int): The robot X position based on the current grid context
    y (int): The robot Y position based on the current grid context
    direction (enum Orientation):  The current orientation of the robot.
    """

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = self.set_direction(direction)

    def set_direction(self, direction):
        """
        Set robot direction

        Parameters:
        direction (enum Orientation): Change robot orientation

        Returns:
        enum Orientation
        """

        err_msg = f'Invalid direction. Valid values (case insensitive): {list(Orientation.__members__)}'
        if direction not in Orientation.__members__:
            raise ValueError(err_msg)

        self.direction = Orientation[direction]

        return self.direction

    def right(self):
        """
        Rotate robot 90deg turn to the right
        """
        self.direction = self.direction.right()

    def left(self):
        """
        Rotate robot 90deg turn to the left
        """
        self.direction = self.direction.left()

    def move(self):
        """
        Move robot position 1 unit forward
        """
        self.x += self.direction.value[0]
        self.y += self.direction.value[1]

    def get_next_position(self):
        """
        Get the x,y position when robot moves forward.

        Returns:
        x (int): The next X position
        y (int): The next Y position
        """

        x = self.x + self.direction.value[0]
        y = self.y + self.direction.value[1]

        return x, y

    def report(self):
        """
        Shows the current x,y position, and direction
        """

        print(f'{self.x},{self.y},{self.direction.name}')
