import re
import pathlib
from collections import Counter
import numpy as np

PUZZLE_DIR = pathlib.Path(__file__).parent
input_file = "input.txt"

lines = (PUZZLE_DIR / input_file).read_text().strip().split("\n")
# print(lines)

points = []
for line in lines:
    point = re.findall("(\d+),(\d+) -> (\d+),(\d+)", line)
    points.append(point)
# print(points)

# grid_size = 1000
# array = np.zeros((grid_size, grid_size))


def add_to_grid(x1, y1, x2, y2, array):
    dx, dy = x2 - x1, y2 - y1
    dir_x, dir_y = 0, 0
    if dx != 0:
        dir_x = dx / abs(dx)
    if dy != 0:
        dir_y = dy / abs(dy)

    for i in range(0, max(abs(dx), abs(dy)) + 1):
        array[y1 + int((i * dir_y))][x1 + int((i * dir_x))] += 1


def part1():
    grid_size = 1000
    array = np.zeros((grid_size, grid_size))
    for row in points:
        x1, y1, x2, y2 = int(row[0][0]), int(row[0][1]), int(row[0][2]), int(row[0][3])
        if x1 == x2 or y1 == y2:
            add_to_grid(x1, y1, x2, y2, array)
        else:
            continue
    return np.count_nonzero(array > 1)


def part2():
    grid_size = 1000
    array = np.zeros((grid_size, grid_size))
    for row in points:
        x1, y1, x2, y2 = int(row[0][0]), int(row[0][1]), int(row[0][2]), int(row[0][3])
        add_to_grid(x1, y1, x2, y2, array)
    return np.count_nonzero(array > 1)


print(f"Answer to part 1 is {part1()}")
print(f"Answer to part 2 is {part2()}")
