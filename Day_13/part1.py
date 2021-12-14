import pathlib
import numpy as np

PUZZLE_DIR = pathlib.Path(__file__).parent

lines = (PUZZLE_DIR / "input.txt").read_text().strip().split('\n\n')[0].split('\n')
instructions = (PUZZLE_DIR / "input.txt").read_text().strip().split('\n\n')[1].split('\n')

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


def fold_array(array, line, axis):

    if axis == 'y':
        foldline = array[line]
        upper_array = array[0:line, :]
        lower_array = array[line+1:, :]
        lower_array = np.flipud(lower_array)
        if lower_array.shape[0] == upper_array.shape[0]:
            added_up = lower_array + upper_array
            count = np.count_nonzero(added_up)
            return added_up, count
        if lower_array.shape[0] > upper_array.shape[0]:
            num_rows = upper_array.shape[0]
            added_up = upper_array + lower_array[0:num_rows]
            lower_array[0:num_rows] = added_up
            count = np.count_nonzero(lower_array)
            return lower_array, count
        else:
            num_rows = lower_array.shape[0]
            added_up = lower_array + upper_array[0:num_rows]
            upper_array[0:num_rows] = added_up
            count = np.count_nonzero(upper_array)
            return upper_array, count
    else:
        left_array = array[: , 0:line]
        right_array = array[:, line+1:]
        right_array = np.fliplr(right_array)
        if right_array.shape[1] > left_array.shape[1]:
            leftarraycols = left_array.shape[1]
            added_up = left_array + right_array[:,leftarraycols*-1:]
            right_array[:,leftarraycols*-1:] = added_up
            count = np.count_nonzero(right_array)
            return right_array, count
        elif right_array.shape[1] == left_array.shape[1]:
            added_up = left_array + right_array
            count = np.count_nonzero(added_up)
            return added_up, count
        else:
            num_of_r_cols = right_array.shape[1]
            added_up = right_array + left_array[:, num_of_r_cols*-1:]
            left_array[:, num_of_r_cols*-1:] =  added_up
            count = np.count_nonzero(left_array)
            return left_array, count


board2, count = fold_array(board, 655, 'x')
print(count)
