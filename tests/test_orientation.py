import sys
import unittest
from pathlib import Path

# TODO: Can this path be removed?
# project_path = Path(__file__).resolve().parents[1]
# sys.path.append( str(project_path) )

from toyrobot.orientation import Orientation


class TestOrientation(unittest.TestCase):

    def setUp(self):
        pass

    def test_right(self):
        test_cases = [
            (Orientation.NORTH, Orientation.EAST),
            (Orientation.EAST, Orientation.SOUTH),
            (Orientation.SOUTH, Orientation.WEST),
            (Orientation.WEST, Orientation.NORTH)
        ]
        for current_orientation, expected in test_cases:
            with self.subTest():
                self.orientation = current_orientation
                self.assertEqual(self.orientation.right(), expected)

    def test_left(self):
        test_cases = [
            (Orientation.NORTH, Orientation.WEST),
            (Orientation.WEST, Orientation.SOUTH),
            (Orientation.SOUTH, Orientation.EAST),
            (Orientation.EAST, Orientation.NORTH)
        ]
        for current_orientation, expected in test_cases:
            with self.subTest():
                self.orientation = current_orientation
                self.assertEqual(self.orientation.left(), expected)

    # TODO: Is this really needed?
    def test_invalid_orientation(self):
        with self.assertRaises(KeyError) as raises:
            Orientation['NON_EXISTENT_ITEM']
        

if __name__ == "__main__":
    unittest.main()