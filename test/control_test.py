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

    def test_simple_move(self):
        commands_from_0_0_to_0_1 = """0 1\n0 0 N\nM"""
        expected = "0 1 N"

        actual = control.launch_mission(commands_from_0_0_to_0_1)

        self.assertEqual(actual, expected)

    def test_move(self):
        self.assertEqual((2, 3), control.execute_move('N', 2, 2))
        self.assertEqual((3, 2), control.execute_move('E', 2, 2))
        self.assertEqual((2, 1), control.execute_move('S', 2, 2))
        self.assertEqual((1, 2), control.execute_move('W', 2, 2))

    def test_turn_right(self):
        self.assertEqual('E', control.execute_turn('N', 'R'))
        self.assertEqual('S', control.execute_turn('E', 'R'))
        self.assertEqual('W', control.execute_turn('S', 'R'))
        self.assertEqual('N', control.execute_turn('W', 'R'))

    def test_turn_left(self):
        self.assertEqual('W', control.execute_turn('N', 'L'))
        self.assertEqual('S', control.execute_turn('W', 'L'))
        self.assertEqual('E', control.execute_turn('S', 'L'))
        self.assertEqual('N', control.execute_turn('E', 'L'))
