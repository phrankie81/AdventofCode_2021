import re
import pathlib
from collections import Counter

PUZZLE_DIR = pathlib.Path(__file__).parent
input_file = "example.txt"


with open(PUZZLE_DIR / input_file) as f:
    data = f.read()


def solution(data, part=1):
    lines = re.findall("(\d+),(\d+) -> (\d+),(\d+)", data)
    points = Counter()
    for line in lines:
        x1, y1, x2, y2 = map(int, line)
        if part == 1 and x1 != x2 and y1 != y2:  # diagonal line
            continue
        dx, dy = x2 - x1, y2 - y1
        length = max(abs(dx), abs(dy))
        x_step, y_step = dx // length, dy // length
        points.update((x1 + i * x_step, y1 + i * y_step) for i in range(length + 1))
    return sum(count > 1 for count in points.values())


# print('Part 1:', solution(data, part=1))

print("Part 2:", solution(data, part=2))
