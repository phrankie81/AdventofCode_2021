import re
from pathlib import Path

PUZZLE_DIR = Path(__file__).parent
entries = (PUZZLE_DIR / "input.txt").read_text().strip()


def wire_connection(signal: list) -> dict:
    known_numbers = {}
    # declare the easy digits
    for item in signal:
        item = "".join(sorted(item))
        if len(item) == 2:
            known_numbers[1] = item
        if len(item) == 4:
            known_numbers[4] = item
        if len(item) == 3:
            known_numbers[7] = item
        if len(item) == 7:
            known_numbers[8] = item

    # find the difference between 4 and 1
    diff_btw_four_and_one = set(known_numbers[4]) - set(known_numbers[1])

    # checks for the 5 segment numbers (can only be 3, 5 or 2)
    five_letter_items = ["".join(sorted(item)) for item in signal if len(item) == 5]
    for item in five_letter_items:
        if set(known_numbers[1]).issubset(set(item)):
            known_numbers[3] = item
        elif diff_btw_four_and_one.issubset(set(item)):
            known_numbers[5] = item
        else:
            known_numbers[2] = item

    # checks for the 6 segment numbers (can only be 9, 6 or 0)
    six_letter_items = ["".join(sorted(item)) for item in signal if len(item) == 6]
    for item in six_letter_items:
        if set(known_numbers[4]).issubset(set(item)):
            known_numbers[9] = item
        elif diff_btw_four_and_one.issubset(set(item)):
            known_numbers[6] = item
        else:
            known_numbers[0] = item

    # swap key and value for
    known_numbers = {v: k for k, v in known_numbers.items()}
    return known_numbers


def part1(entries):
    count = 0
    for line in entries.split("\n"):
        digits = re.findall(".+ \| (\w+) (\w+) (\w+) (\w+)", line)
        digits = digits[0]
        for digit in digits:
            if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                count += 1
    return count


def part2(entries):
    output = 0
    for line in entries.split("\n"):
        row = re.findall("(.+) \| (\w+) (\w+) (\w+) (\w+)", line)
        signal = row[0][0].split()
        digits = re.findall(".+ \| (\w+) (\w+) (\w+) (\w+)", line)
        digits = ["".join(sorted(digit)) for digit in digits[0]]
        decoded = wire_connection(signal)
        digits = [str(decoded[digit]) for digit in digits]
        nums = "".join(digits)
        output += int(nums)
    return output


print(f"Answer to part 1 is {part1(entries)}")
print(f"Answer to part 2 is {part2(entries)}")
