def find_empty(puzzle):
    for r in range(9): # scan board
        for c in range(9):
            if puzzle[r][c] == -1: 
                return r, c # return location of empty space
    return None, None

def is_valid(puzzle, guess, row, col):
    # rows
    row_vals = puzzle[row]
    if guess in row_vals: 
        return False # guess found in row
    
    # columns
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False # guess found in column

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3): #scan
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False # guess found in location
    
    return True


def solve(puzzle):
    row, col = find_empty(puzzle)

    if row is None:
        return True

    for guess in range(1, 10): # nums from 1 to 9 (included)
        if is_valid(puzzle, guess, row, col): 
            puzzle[row][col] = guess # set correct guess in location

            if solve(puzzle): # keep guessing
                return True

        puzzle[row][col] = -1 # if not guessed keep blank
    
    return False # sudoku cannot be resolved

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve(example_board))
    print(example_board)