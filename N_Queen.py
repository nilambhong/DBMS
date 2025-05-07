def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_board(board, n)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(board, row + 1, n)
            board[row] = -1  # backtrack

def print_board(board, n):
    for i in range(n):
        row = ['.'] * n
        if board[i] != -1:
            row[board[i]] = 'Q'
        print("".join(row))
    print("\n" + "-" * (2 * n - 1))

# Example: Solve for N-Queens
n = 4 # Change to 8 for 8-Queens
board = [-1] * n
print("Solutions for N-Queens Problem:")
solve_n_queens(board, 0, n)
