import logging
import operator
from toyrobot.orientation import Orientation


class Robot():

    x = property(operator.attrgetter('_x'))
    y = property(operator.attrgetter('_y'))

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = self.set_direction(direction)

    @x.setter
    def x(self, val):
        try:
            val = int(val)
        except ValueError:
            raise ValueError('Not allowed. X position must be integer')

        self._x = val

    @y.setter
    def y(self, val):
        try:
            val = int(val)
        except ValueError:
            raise ValueError('Not allowed. Y position must be integer')

        self._y = val

    def set_direction(self, direction):
        err_msg = f'Invalid direction. Valid values (case insensitive): {list(Orientation.__members__)}'
        if direction not in Orientation.__members__:
            raise ValueError(err_msg)

        self.direction = Orientation[direction]

        return self.direction

    def right(self):
        self.direction = self.direction.right()

    def left(self):
        self.direction = self.direction.left()

    def move(self):
        self.x += self.direction.value[0]
        self.y += self.direction.value[1]

    def get_next_position(self):
        x = self.x + self.direction.value[0]
        y = self.y + self.direction.value[1]

        return x, y

    def report(self):
        print(f'{self.x},{self.y},{self.direction.name}')
