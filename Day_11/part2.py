import fileinput, re
from pathlib import Path
import pprint
import numpy as np


PUZZLE_DIR = Path(__file__).parent

data = [
    [11] + [int(x) for x in re.findall("\d", line)] + [11]
    for line in fileinput.input(PUZZLE_DIR / "input.txt")
]
data.insert(0, [11] * len(data[0]))
data.append([11] * len(data[0]))

       

def find_tens(board, flashes):
    if any(10 in x for x in board[1:-1]):
        for r in range(1, len(board) - 1):
            for c in range(1, len(board[r]) - 1):
                if board[r][c] == 10:
                    board[r][c] = 0
                    flashes += 1
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]:
                        if board[r + dr][c + dc] != 10 and board[r + dr][c + dc] != 0:
                            board[r + dr][c + dc] += 1
        return find_tens(board, flashes)
        
    else:
        return board, flashes

flashes = 0
for step in range (1, 500):
    # increase all in the data by 1
    for r in range(1, len(data) - 1):
        for c in range(1, len(data[r]) - 1):
            data[r][c] += 1
    data, flashes = find_tens(data, flashes)
    # check real board
    real_board = np.array(data)
    real_board = real_board[1:-1, 1:-1]
    if np.all((np.array(real_board)) == 0):
        break
        
    
print(step)
print(real_board)