# Todos:
# [1] enable ai 
# [x] bigger boards
# [0] coordinates around boards
# [0] different ships

import random
import numpy

# The types of ships

SHIPS = {'Destroyer': 2, 'Submarine': 3, 'Battleship': 4}

# Creates the board 

def create_board(size):
    return [['~'] * size for _ in range(size)]

# Prints the board in the terminal 

def print_board(board):
    i = 1
    print(' ',1,2,3,4,5)
    for row in board:
        
        print(i,' '.join(row))
        i = i +1
    print()

# Random ship placement using

def place_ships(board, num_ships):
    ships = 0
    while ships < num_ships:
        x, y = random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)
        if board[x][y] == '~':
            board[x][y] = 'S'
            ships += 1

# Place ships randomly while keeping them on the field. 

# def place_ship(ship, size, grid):

#   # Randomly generate row, col index for head of ship
#   row = random_row()
#   col = random_col()

#   # Randomly choose vertical or horizontal orientation
#   is_vertical = random.choice([True, False])

#   if is_vertical:
#     if row + size > GRID_SIZE:
#       return False

#     for i in range(size):
#       grid[row+i][col] = ship[0]

#   else:
#     if col + size > GRID_SIZE:
#       return False

#     for i in range(size):
#       grid[row][col+i] = ship[0]

#   return True

# User input and input validator

def get_user_guess(board):
    while True:
        guess = input("Enter your guess (row and column, e.g., 2 3): ").split()
        if len(guess) == 2 and guess[0].isdigit() and guess[1].isdigit() and int(guess[0])<(board) and int(guess[1])<(board):
            return int(guess[0])-1, int(guess[1])-1
        else:
            print("Invalid input. Please enter two numbers separated by a space.")

# Random enemy move

def get_enemy_guess(board):
    guess = random.randint(0, board - 1), random.randint(0, board - 1)
    return int(guess[0]), int(guess[1])

# Sets up the players and computers boards for the game

def setup_game(board_size, num_ships):
    player1_board = create_board(board_size)
    enemy_board = create_board(board_size)
    
    print("The player's ships have been placed:")
    place_ships(player1_board, num_ships)
    print_board(player1_board)
    
    print("The enemy has placed their ships:")
    
    return player1_board, enemy_board

# The main game run function

def play_game():
    board_size = 5
    num_ships = 3
    player1_board, enemy_board = setup_game(board_size, num_ships)
    player1_guesses = create_board(board_size)
    enemy_guesses = create_board(board_size)
    
    player1_ships = num_ships
    enemy_ships = num_ships
    turn = 0
    
    while player1_ships > 0 and enemy_ships > 0:
        if turn % 2 == 0:
            print("Players turn")
            print_board(player1_guesses)
            guess = get_user_guess(board_size)
            if enemy_board[guess[0]][guess[1]] == 'S':
                print("You hit!")
                player1_guesses[guess[0]][guess[1]] = 'X'
                enemy_board[guess[0]][guess[1]] = 'X'
                enemy_ships -= 1
            else:
                print("You missed.")
                print("---")
                player1_guesses[guess[0]][guess[1]] = 'O'
        else:
            print("Enemys turn")
            print_board(enemy_guesses)
            guess = get_enemy_guess(board_size)
            if player1_board[guess[0]][guess[1]] == 'S':
                print("Enemy has hit you!")
                enemy_guesses[guess[0]][guess[1]] = 'X'
                player1_board[guess[0]][guess[1]] = 'X'
                player1_ships -= 1
            else:
                print("Enemy Missed!")
                print("---")
                enemy_guesses[guess[0]][guess[1]] = 'O'
        
        turn += 1
    
    if player1_ships == 0:
        print("Enemy wins!")
    else:
        print("Player 1 wins!")

if __name__ == "__main__":
    play_game()


