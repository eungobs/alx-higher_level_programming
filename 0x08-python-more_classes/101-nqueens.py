#!/usr/bin/python3
"""
Solves the N-queens puzzle.
"""
import sys

def is_safe(board, row, col, n):
    """Checks if placing a queen at a given position is safe."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, col, n):
    """Solves the N Queens problem."""
    if col >= n:
        print_board(board, n)
        return True
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_n_queens(board, col + 1, n) or res
            board[i][col] = 0
    return res

def print_board(board, n):
    """Prints the board configuration."""
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()

if __name__ == "__main__":
    # Parse command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [[0 for x in range(n)] for y in range(n)]

    # Solve the problem
    solve_n_queens(board, 0, n)
