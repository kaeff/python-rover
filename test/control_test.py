import unittest

from rover import control


class ControlTest(unittest.TestCase):

    def test_example(self):
        input = """5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM"""
        expected = """1 3 N
5 1 E"""

        actual = control.launch_mission(input)

        self.assertEqual(actual, expected)
