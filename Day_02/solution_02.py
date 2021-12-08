# aoc_template.py

import pathlib
import sys

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input_file: str) -> list:
    """Parse input from txt file"""
    input_lines = (PUZZLE_DIR/puzzle_input_file).read_text().strip()
    return[[line.split(" ")[0], int(line.split(" ")[1])] for line in input_lines.split("\n")]
    

def part1(puzzle_input_file: str):
    """Solve part 1"""
    commands = parse(puzzle_input_file)
    horizontal_pos, depth = 0, 0
    for [command, val] in commands:
        if command == 'forward':
            horizontal_pos += val
        if command == 'down':
            depth += val
        if command == 'up':
            depth -= val
    return horizontal_pos * depth

def part2(puzzle_input_file: str):
    """Solve part 2"""
    commands = parse(puzzle_input_file)
    horizontal_pos, depth, aim = 0, 0, 0
    for [command, val] in commands:
        if command == 'forward':
            horizontal_pos += val
            depth += val * aim
        if command == 'down':
            aim += val
        if command == 'up':
            aim -= val
    return horizontal_pos * depth
    

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    # data = parse(puzzle_input)
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)

    return solution1, solution2


if __name__ == '__main__':
    puzzle_input = "input1.txt"
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

# to use command line to run puzzles
# if __name__ == "__main__":
#     for path in sys.argv[1:]:
#         print(f"{path}:")
#         puzzle_input = pathlib.Path(path).read_text().strip()
#         solutions = solve(puzzle_input)
#         print("\n".join(str(solution) for solution in solutions))