import os
import unittest

from main import solve


class TestMain(unittest.TestCase):

    def test_solve(self):
        """
        Any method which starts with `test_` will be considered as a test case.
        """
        try:
            with open('input_test') as file:
                test_input = file.read()
        except FileNotFoundError:
            day = os.getcwd().split('/')[-1]
            print('No test input, drum some up from: ' +
                  f'https://adventofcode.com/2022/day/{day}')

        res = solve(test_input)
        self.assertEqual(res, '0')


if __name__ == '__main__':
    unittest.main()
