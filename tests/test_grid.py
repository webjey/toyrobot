import sys
import unittest
from pathlib import Path

# project_path = Path(__file__).resolve().parents[1]
# sys.path.append( str(project_path) )

from toyrobot.robot import Robot
from toyrobot.grid import Grid


class TestGrid(unittest.TestCase):

    def setUp(self):
        self.grid = Grid(cols=5, rows=5)

    def test_add_and_get_robot(self):
        robot = Robot(2, 3, 'SOUTH')
        self.grid.add_robot(robot)
        self.assertEqual(self.grid.robot, robot)
        self.assertEqual(self.grid.get_robot(), robot)

    def test_has_robot(self):
        robot = Robot(2, 3, 'SOUTH')
        self.grid.add_robot(robot)
        self.assertEqual(self.grid.has_robot(), True)

    def test_is_valid(self):
        self.assertEqual(self.grid.is_valid(4, 4), True)
        self.assertEqual(self.grid.is_valid(5, 5), False)


if __name__ == "__main__":
    unittest.main()