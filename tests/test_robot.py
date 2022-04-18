import sys
import unittest
from pathlib import Path

# TODO: Can this path be removed?
# project_path = Path(__file__).resolve().parents[1]
# sys.path.append( str(project_path) )

from toyrobot.robot import Robot
from toyrobot.orientation import Orientation


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.robot = Robot(2, 3, 'SOUTH')

    def test_right(self):
        self.robot.right()
        self.assertEqual(self.robot.x, 2)
        self.assertEqual(self.robot.y, 3)
        self.assertEqual(self.robot.direction, Orientation.WEST)

    def test_left(self):
        self.robot.left()
        self.assertEqual(self.robot.x, 2)
        self.assertEqual(self.robot.y, 3)
        self.assertEqual(self.robot.direction, Orientation.EAST)

    def test_move(self):
        self.robot.move()
        self.assertEqual(self.robot.y, 2)

    def test_get_next_position(self):
        self.robot.move()
        self.assertEqual(self.robot.y, 2)


if __name__ == "__main__":
    unittest.main()