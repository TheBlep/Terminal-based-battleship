
import random

def create_board(size):
    return [['~'] * size for _ in range(size)]

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def place_ships(board, num_ships):
    ships = 0
    while ships < num_ships:
        x, y = random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)
        if board[x][y] == '~':
            board[x][y] = 'S'
            ships += 1

