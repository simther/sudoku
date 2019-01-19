# Example fo a Sudoku: 000000082000001906320000000000086450000005200651340800030914020090050178100800300

grid = input("Just input your sudoku from top to bottom, from left to right.\n> ")
grid_list = []

if len(grid) < 81:
    print("Not a valid sudoku!")

else:
    for char in range(0, 81, 9):
        grid_list.append(list(grid[char:char+9]))
    for row in range(0, 9):
        for col in range(0, 9):
            grid_list[row][col] = int(grid_list[row][col])

def check_if_valid_number(num, row, col):
    for i in range(0, 9):
        if grid_list[row][i] == num:
            return False
    for i in range(0, 9):
        if grid_list[i][col] == num:
            return False
    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if grid_list[i][j] == num:
                return False
    return True

def find_empty_cell(row, col):
    for r in range(0, 9):
        for c in range(0, 9):
            if grid_list[r][c] == 0:
                empty_cell = [r, c, 1]
                return empty_cell
    empty_cell = [-1, -1, 0]
    return empty_cell

def solving_sudoku():
    row = 0
    col = 0
    cell = find_empty_cell(row, col)
    if cell[2] == 0:
        return True
    row = cell[0]
    col = cell[1]
    for i in range(1,10):
        if check_if_valid_number(i, row, col):
            grid_list[row][col] = i
            if solving_sudoku():
                return True
            grid_list[row][col] = 0
    return False

if solving_sudoku():
    for row in grid_list:
        print(row)
else:
    print("No solution")
