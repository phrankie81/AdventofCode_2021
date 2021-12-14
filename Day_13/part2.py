import re
import pathlib
import numpy as np
import sys
from matplotlib import pyplot as plt


PUZZLE_DIR = pathlib.Path(__file__).parent
file = 'input.txt'

lines = (PUZZLE_DIR / file).read_text().strip().split('\n\n')[0].split('\n')
instructions = (PUZZLE_DIR / file).read_text().strip().split('\n\n')[1].split('\n')

row, col = 0, 0

for line in lines:
    line = line.split(',')
    r, c = int(line[1]), int(line[0])
    if r > row:
        row = r
    if c > col:
        col = c

row_size = row + 1
col_size = col + 1
board = np.zeros((row_size, col_size))
board = board.astype(int)

for line in lines:
    line = line.split(',')
    r, c = int(line[1]), int(line[0])
    board[r][c] = 1


countlist = []

def fold_array(array, instructions):
    for instruction in instructions:
        instruction = instruction.replace('fold along ', '')
        instruction = instruction.split('=')
        axis, line = instruction[0], int(instruction[1])
        if axis == 'y':
            upper_array = array[0:line, :]
            lower_array = array[line+1:, :]
            lower_array = np.flipud(lower_array)
            if lower_array.shape[0] == upper_array.shape[0]:
                added_up = lower_array + upper_array
                count = np.count_nonzero(added_up)
                countlist.append(count)
                array = added_up
                array[array > 0] = 1
                plt.imshow(array)
                plt.show()
            elif lower_array.shape[0] > upper_array.shape[0]:
                num_rows = upper_array.shape[0]
                added_up = upper_array + lower_array[0:num_rows]
                lower_array[0:num_rows] = added_up
                count = np.count_nonzero(lower_array)
                countlist.append(count)
                array = lower_array
                plt.imshow(array)
                plt.show()
            else:
                num_rows = lower_array.shape[0]
                added_up = lower_array + upper_array[0:num_rows]
                upper_array[0:num_rows] = added_up
                count = np.count_nonzero(upper_array)
                countlist.append(count)
                array = upper_array
                plt.imshow(array)
                plt.show()
        else:
            left_array = array[: , 0:line]
            right_array = array[:, line+1:]
            right_array = np.fliplr(right_array)
            if right_array.shape[1] > left_array.shape[1]:
                leftarraycols = left_array.shape[1]
                added_up = left_array + right_array[:,leftarraycols*-1:]
                right_array[:,leftarraycols*-1:] = added_up
                count = np.count_nonzero(right_array)
                countlist.append(count)
                array = right_array
                plt.imshow(array)
                plt.show()
            elif right_array.shape[1] == left_array.shape[1]:
                added_up = left_array + right_array
                count = np.count_nonzero(added_up)
                countlist.append(count)
                array = added_up
                plt.imshow(array)
                plt.show()
            else:
                num_of_r_cols = right_array.shape[1]
                added_up = right_array + left_array[:, num_of_r_cols*-1:]
                left_array[:, num_of_r_cols*-1:] =  added_up
                count = np.count_nonzero(left_array)
                countlist.append(count)
                array = left_array
                plt.imshow(array)
                plt.show()


fold_array(board, instructions)
