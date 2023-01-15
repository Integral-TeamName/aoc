def main():
    with open("input") as file:
        elf_strings = file.read().split("\n\n")
        elf_calories = sorted(
            [sum([int(x) for x in elf.split("\n")]) for elf in elf_strings]
        )
    print(f"part 1: {elf_calories[-1]}")
    print(f"part 2: {sum(elf_calories[-3:])}")


if __name__ == "__name__":
    main()
