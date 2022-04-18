from enum import Enum

class Orientation(Enum):

    NORTH = ( 0, 1)
    EAST  = ( 1, 0)
    SOUTH = ( 0,-1)
    WEST  = (-1, 0)

    def right(self):
        all_element = list(self.__class__)
        index = all_element.index(self) + 1
        if index >= len(all_element):
            index = 0
        return all_element[index]

    def left(self):
        all_element = list(self.__class__)
        index = all_element.index(self) - 1
        if index < 0:
            index = len(all_element) - 1
        return all_element[index]

