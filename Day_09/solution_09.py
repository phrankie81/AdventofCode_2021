import fileinput, re
from pathlib import Path
from math import prod


PUZZLE_DIR = Path(__file__).parent

# pad the board with 9s to make checking edges and corners easier
data = [
    [9] + [int(x) for x in re.findall("\d", line)] + [9]
    for line in fileinput.input(PUZZLE_DIR / "input.txt")
]
data.insert(0, [9] * len(data[0]))
data.append([9] * len(data[0]))


def basins(board, row, col, done=set()):
    if board[row][col] == 9 or (row, col) in done:
        return 0
    done.add((row, col))
    return 1 + sum(
        basins(board, row + dr, col + dc, done)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]
    )


pt1, pt2 = 0, []
for r in range(1, len(data) - 1):
    for c in range(1, len(data[r]) - 1):
        if all(
            data[r][c] < data[r + dr][c + dc]
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ):
            pt1 += data[r][c] + 1
            pt2.append(basins(data, r, c))
print(f"Answer to part 1 is {pt1}")
print(f"Answer to part 2 is {prod(sorted(pt2)[-3:])}")
