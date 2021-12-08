# aoc_template.py

from pathlib import Path

PUZZLE_DIR = Path(__file__).parent
puzzle_input = (PUZZLE_DIR/"example1.txt").read_text().strip()
data = [int(line) for line in puzzle_input.split("\n")]
print(data)

def part1(data):
    """Solve part 1"""
    num_of_increases = 0
    for i in range(len(data)-1):
        if data[i] - data[i+1] < 0:
            num_of_increases += 1
    return num_of_increases


def part2(data):
    """Solve part 2"""
    the_sums = [data[i]+data[i+1]+data[i+2] for i in range(len(data)-2)]
    result = part1(the_sums)
    return result


if __name__ == '__main__':
    print(f"The answer to part 1 is {part1(data)}")
    print(f'The answer to part 2 is {part2(data)}')

