# aoc_template.py

import pathlib
import sys

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split("\n")]

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

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == '__main__':
    puzzle_input = (PUZZLE_DIR/"example1.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

# to use command line to run puzzles
# if __name__ == "__main__":
#     for path in sys.argv[1:]:
#         print(f"{path}:")
#         puzzle_input = pathlib.Path(path).read_text().strip()
#         solutions = solve(puzzle_input)
#         print("\n".join(str(solution) for solution in solutions))