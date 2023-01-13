import os


def main():
    try:
        with open("input") as file:
            puzzle_input = file.read()
    except FileNotFoundError:
        day = os.getcwd().split('/')[-1]
        print('Input file not found, get its contents here: ',
              f'https://adventofcode.com/2022/day/{day}/input')
        return 0

    print(f'part 1: {solve(puzzle_input)}')
    print(f'part 2: {solve(puzzle_input, part=2)}')

    return 1


def solve(puzzle_input: str, part: int = 1) -> str:
    """
    Our main solve method.
    """

    # solution goes here

    return '0'


if __name__ == '__main__':
    main()
