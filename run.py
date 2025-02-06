# Todos:
# enable ai
# bigger boards
# coordinates around boards
# different ships

# Notes:
# stick with random placement


import random

# Creates the board 

def create_board(size):
    return [['~'] * size for _ in range(size)]

# Prints the board in the terminal 

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()
    print(1,2,3,4,5)

# Random ship placement using

def place_ships(board, num_ships):
    ships = 0
    while ships < num_ships:
        x, y = random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)
        if board[x][y] == '~':
            board[x][y] = 'S'
            ships += 1

# User input and input validator

def get_user_guess():
    while True:
        guess = input("Enter your guess (row and column, e.g., 2 3): ").split()
        if len(guess) == 2 and guess[0].isdigit() and guess[1].isdigit():
            return int(guess[0]), int(guess[1])
        else:
            print("Invalid input. Please enter two numbers separated by a space.")

# Sets up the players and computers boards for the game

def setup_game(board_size, num_ships):
    player1_board = create_board(board_size)
    player2_board = create_board(board_size)
    
    print("Player 1, place your ships:")
    place_ships(player1_board, num_ships)
    print_board(player1_board)
    
    print("Player 2, place your ships:")
    place_ships(player2_board, num_ships)
    print_board(player2_board)
    
    return player1_board, player2_board

# The main game run function

def play_game():
    board_size = 5
    num_ships = 3
    player1_board, player2_board = setup_game(board_size, num_ships)
    player1_guesses = create_board(board_size)
    player2_guesses = create_board(board_size)
    
    player1_ships = num_ships
    player2_ships = num_ships
    turn = 0
    
    while player1_ships > 0 and player2_ships > 0:
        if turn % 2 == 0:
            print("Player 1's turn")
            print_board(player1_guesses)
            guess = get_user_guess()
            if player2_board[guess[0]][guess[1]] == 'S':
                print("Hit!")
                player1_guesses[guess[0]][guess[1]] = 'X'
                player2_board[guess[0]][guess[1]] = 'X'
                player2_ships -= 1
            else:
                print("Miss.")
                player1_guesses[guess[0]][guess[1]] = 'O'
        else:
            print("Player 2's turn")
            print_board(player2_guesses)
            guess = get_user_guess()
            if player1_board[guess[0]][guess[1]] == 'S':
                print("Hit!")
                player2_guesses[guess[0]][guess[1]] = 'X'
                player1_board[guess[0]][guess[1]] = 'X'
                player1_ships -= 1
            else:
                print("Miss.")
                player2_guesses[guess[0]][guess[1]] = 'O'
        
        turn += 1
    
    if player1_ships == 0:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

if __name__ == "__main__":
    play_game()


