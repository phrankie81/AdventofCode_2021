import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input_file: str) -> list:
    """Parse input from txt file"""
    input_lines = (PUZZLE_DIR/puzzle_input_file).read_text().strip().split("\n")
    return input_lines
    

def part1(puzzle_input_file: str):
    """Solve part 1"""
    lines = parse(puzzle_input_file)
    gamma_rate_str, epsilon_rate_str = '', ''
    for i in range(len(lines[1])):
        column_list = [line[i] for line in lines]
        gamma_rate_str += max(set(column_list), key = column_list.count)
        epsilon_rate_str += min(set(column_list), key = column_list.count)
    return int(gamma_rate_str, 2) * int(epsilon_rate_str, 2)


def extract_rating(puzzle_input, type_of_rating: int):
    rating = parse(puzzle_input)
    
    for i in range(len(rating)):
        if len(rating) == 1:
            rating = rating
        else:
            column_list = [line[i] for line in rating]
            if column_list.count('1') == column_list.count('0'):
                bits = str(type_of_rating)
            elif type_of_rating == 1:
                bits = max(set(column_list), key = column_list.count)
            else:
                bits = min(set(column_list), key = column_list.count)
            rating = list(filter(lambda line: line[i] == bits, rating))
    return rating


def part2(puzzle_input_file: str):
    """Solve part 2"""
    oxygen_gen_rating = extract_rating(puzzle_input_file, 1)
    co2_scrubber_rating = extract_rating(puzzle_input_file, 0)
    return int(oxygen_gen_rating[0], 2) * int(co2_scrubber_rating[0], 2)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    # data = parse(puzzle_input)
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)

    return solution1, solution2


if __name__ == '__main__':
    puzzle_input = "input.txt"
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
