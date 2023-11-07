def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0
    return False
    
def print_board(board):
    for row in board:
        print(" ".join(["Q" if x else "." for x in row]))

def place_first_queen(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[0][0] = 1

    if solve_n_queens(board, 1):
        print("Solution found:")
        print_board(board)
        print(len(board))
    else:
        print("No solution exists.")

n = int(input("Enter the size of the chessboard (e.g., 8): "))
place_first_queen(n)
    
