import os

chars = "abcdefghijklmnopqrstuvwxyz"
chars += chars.upper()
char_map = {char: i + 1 for i, char in dict(enumerate(chars)).items()}


def main():
    try:
        with open("input") as file:
            puzzle_input = file.read()
    except FileNotFoundError:
        day = os.getcwd().split("/")[-1]
        print(
            "Input file not found, get its contents here: ",
            f"https://adventofcode.com/2022/day/{day}/input",
        )
        return 0

    print(f"part 1: {solve(puzzle_input)}")
    print(f"part 2: {solve(puzzle_input, part=2)}")

    return 1


def solve(puzzle_input: str, part: int = 1) -> str:
    rucksacks = puzzle_input.split("\n")
    priorities = 0
    if part == 2:
        groups = []
        for i in range(int(len(rucksacks) / 3)):
            groups.append(rucksacks[i * 3 : (i + 1) * 3])
        for group in groups:
            a, b, c = group
            for char in a:
                if char in b and char in c:
                    priorities += char_map[char]
                    break
    else:
        for rucksack in rucksacks:
            compartment_length = int(len(rucksack) / 2)
            left, right = (
                rucksack[:compartment_length],
                rucksack[compartment_length:],
            )

            for char in left:
                if char in right:
                    priorities += char_map[char]
                    break
    return str(priorities)


if __name__ == "__main__":
    main()
