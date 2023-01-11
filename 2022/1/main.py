def main():
    with open("input.txt") as file:
        elf_strings = file.read().split('\n\n')
        elf_max_calories = sorted([sum([int(x) for x in elf.split('\n')]) for elf in elf_strings])
    print(f'Elf with the largest calories: {elf_max_calories[-1]}')
    print(f'Sum of the three largest calories among the elvers: {sum(elf_max_calories[-3:])}')


main()
