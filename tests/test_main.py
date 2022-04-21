import unittest
import sys
import io
import argparse

from toyrobot.__main__ import parse_args, main

class Test__Main__(unittest.TestCase):

    def setUp(self):
        pass

    def test_parse_args(self):
        test_cases = [
            (['--file',    'tests/data/1.txt'], 
              ('tests/data/1.txt', 5, 5)),   # default rows & cols is 5

            (['--file',    'tests/data/1.txt',
              '--rows',    '1',
              '--columns', '2'], 
              ('tests/data/1.txt', 1, 2)),

            ]
        for args, expected in test_cases:
            parsed = parse_args(args)
            self.assertEqual( (parsed.file, parsed.rows, parsed.columns),  expected)

    def test_parse_args_non_existent_file(self):
        args = ['--file', 'non_existent_file.txt']

        capturedOutput = io.StringIO()
        sys.stderr = capturedOutput

        with self.assertRaises(SystemExit):
            parse_args(args)

    def test_main(self):
        test_cases = [
            (['--file', 'tests/data/1.txt'], ''),
            (['--file', 'tests/data/2.txt'], '2,2,SOUTH\n'),
            (['--file', 'tests/data/3.txt'], '2,3,EAST\n')
        ]
        for args, expected in test_cases:
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            main(args)
            
            self.assertEqual(capturedOutput.getvalue(), expected)
            


if __name__ == "__main__":
    unittest.main()