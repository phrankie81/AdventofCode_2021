import pathlib
import numpy as np

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse(puzzle_input_file: str):
    draw_numbers, *boards = (PUZZLE_DIR / puzzle_input_file).read_text().strip().split("\n\n")
    draw_numbers = [int(n) for n in draw_numbers.split(",")]
    boards = [[[int(n) for n in line.split()] for line in board.split("\n")] for board in boards]
    boards = [np.array(board) for board in boards]

    return draw_numbers, boards


def update(board, num):
    new = board.copy()
    new[new == num] = -1

    return new


def check(board):
    if any(board.sum(0) == -5) or any(board.sum(1) == -5):
        return True
    return False


def part1(input_file):
    draw_numbers, boards = parse(input_file)
    for n in draw_numbers:
        for i in range(len(boards)):
            boards[i] = update(boards[i], n)
            if check(boards[i]):
                result = n * (boards[i][boards[i] != -1].sum()) # many thanks to this genius https://stackoverflow.com/a/25060182
                return result


def part2(input_file):
    draw_numbers, boards = parse(input_file)
    wins = [0] * len(boards)
    for n in draw_numbers:
        for i in range(len(boards)):
            boards[i] = update(boards[i], n)
            if wins[i] == 0 and check(boards[i]):
                result = n * (boards[i][boards[i] != -1].sum())
                wins[i] = 1
                if sum(wins) == len(boards):
                    last = result
                    return last




if __name__ =='__main__':
    puzzle_input = "input.txt"
    part1_solution = part1(puzzle_input)
    part2_solution = part2(puzzle_input)
    print(f"Part 1 solution is {part1_solution}")
    print(f"Part 2 solution is {part2_solution}")
