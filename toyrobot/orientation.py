from enum import Enum

class Orientation(Enum):
    """
    This class handles the valid directions
    The enum tuple values represents the x,y magnitude of change based on direction.
    For the case of robot, 

    NORTH = (0, 1)
             ^  ^---- Y increases by 1 unit
             |------- X increases by 0 unit 

    Usage:
    (x_offset, y_offset) = Orientation['NORTH'].value

    """

    NORTH = ( 0, 1)
    EAST  = ( 1, 0)
    SOUTH = ( 0,-1)
    WEST  = (-1, 0)

    def right(self):
        """
        Increase enum index (the pointer) by 1

        eg.
        direction = Orientation['NORTH']
        direction.right() # Returns Orientation.EAST
        """
        items = list(self.__class__)
        index = items.index(self) + 1
        if index >= len(items):
            index = 0
        return items[index]

    def left(self):
        """
        Decrease enum index by 1
        """

        items = list(self.__class__)
        index = items.index(self) - 1
        if index < 0:
            index = len(items) - 1
        return items[index]

