import os
import unittest

from main import solve


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        try:
            with open("input_test") as file:
                self.test_input = file.read()
        except FileNotFoundError:
            day = os.getcwd().split("/")[-1]
            print(
                "No test input, drum some up from: "
                + f"https://adventofcode.com/2022/day/{day}"
            )

    def test_solve_part_one(self):
        res = solve(self.test_input)

        self.assertEqual(res, "157")

    def test_solve_part_two(self):
        res = solve(self.test_input, part=2)

        self.assertEqual(res, "70")


if __name__ == "__main__":
    unittest.main()
