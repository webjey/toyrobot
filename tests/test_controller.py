import unittest
import sys
import io

from toyrobot.controller import Controller
from toyrobot.grid import Grid
from toyrobot.orientation import Orientation


class TestController(unittest.TestCase):

    def setUp(self):
        self.grid = Grid(cols=5, rows=5)
        self.controller = Controller(grid=self.grid)

    def test_process_command_robot_not_yet_placed(self):
        test_cases = [
            ('PLACE 5,5,NORTH', False), # Out of bound
            ('MOVE',            False),
            ('RIGHT',           False),
            ('LEFT',            False),
            ('REPORT',          False),
            ('PLACE 0,0,NORTH', True ),
        ]
        for cmd, expected in test_cases:
            self.controller.process_command(cmd)
            self.assertEqual(self.grid.has_robot(), expected)

    def test_process_command_left(self):
        test_cases = [
            ('PLACE 0,0,NORTH', (0, 0, Orientation.NORTH)),
            ('LEFT',            (0, 0, Orientation.WEST )),
            ('LEFT',            (0, 0, Orientation.SOUTH)),
            ('LEFT',            (0, 0, Orientation.EAST )),
            ('LEFT',            (0, 0, Orientation.NORTH)),
        ]
        for cmd, expected in test_cases:
            self.controller.process_command(cmd)
            self.assertEqual((self.grid.get_robot().x,
                              self.grid.get_robot().y,
                              self.grid.get_robot().direction), expected)

    def test_process_command_right(self):
        test_cases = [
            ('PLACE 0,0,NORTH', (0, 0, Orientation.NORTH)),
            ('RIGHT',           (0, 0, Orientation.EAST )),
            ('RIGHT',           (0, 0, Orientation.SOUTH)),
            ('RIGHT',           (0, 0, Orientation.WEST )),
            ('RIGHT',           (0, 0, Orientation.NORTH)),
        ]
        for cmd, expected in test_cases:
            self.controller.process_command(cmd)
            self.assertEqual((self.grid.get_robot().x,
                              self.grid.get_robot().y,
                              self.grid.get_robot().direction), expected)

    def test_process_command_move(self):
        test_cases = [
            (['PLACE 0,0,NORTH', 'MOVE'], (0, 1)),
            (['PLACE 0,0,EAST' , 'MOVE'], (1, 0)),
            (['PLACE 4,4,SOUTH', 'MOVE'], (4, 3)),
            (['PLACE 4,4,WEST' , 'MOVE'], (3, 4)),
        ]
        for cmds, expected in test_cases:
            for cmd in cmds:
                self.controller.process_command(cmd)

            self.assertEqual((self.grid.get_robot().x,
                              self.grid.get_robot().y), expected)

    def test_process_command_move_out_of_bound(self):
        test_cases = [
            (['PLACE 0,0,SOUTH', 'MOVE'], (0, 0)),
            (['PLACE 0,0,WEST' , 'MOVE'], (0, 0)),
            (['PLACE 4,4,NORTH', 'MOVE'], (4, 4)),
            (['PLACE 4,4,EAST' , 'MOVE'], (4, 4)),
        ]
        for cmds, expected in test_cases:
            for cmd in cmds:
                self.controller.process_command(cmd)
                self.assertEqual((self.grid.get_robot().x,
                                  self.grid.get_robot().y), expected)

    def test_process_command_report(self):
        test_cases = [
            (['PLACE 5,5,NORTH', 'REPORT'], ''           ), # out of bound
            (['PLACE 1,1,NORTH', 'REPORT'], '1,1,NORTH\n'),
            (['PLACE 5,5,NORTH', 'REPORT'], '1,1,NORTH\n'),
        ]
        for cmds, expected in test_cases:
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            for cmd in cmds:
                self.controller.process_command(cmd)

            self.assertEqual(capturedOutput.getvalue(), expected)

        
if __name__ == "__main__":
    unittest.main()