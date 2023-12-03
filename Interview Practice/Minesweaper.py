"""

Write a function that will take 3 arguments:
bombs = list of bomb locations
rows
columns
mine_sweeper([[0, 0], [1, 2], 3, 4])

arg1: bomb at row index 0, column index 0
      bomb at row index 0, column index 1
arg2: 3 rows
arg3: 4 columns

We should return an 3x4 array = bomb
output:
[[-1, 2, 1, 1],
[1, 2, -1, 1],
[0, 1, 1, 1]]

"""


def mine_sweeper(bombs, num_rows, num_columns):
    field = [[0 for i in range(num_columns)] for j in range(num_rows)]
    for bomb_location in bombs:
        (bomb_row, bomb_col) = bomb_location
        field[bomb_row][bomb_col] = -1

        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for i in row_range:
            current_i = i
            for j in col_range:
                current_j = j
                if 0 <= i < num_rows and 0 <= j < num_columns and field[i][j] != -1:
                    field[i][j] += 1

    return field


arr = [[0, 0], [1, 2]]
rows = 3
cols = 4
print(mine_sweeper(arr, rows, cols))
