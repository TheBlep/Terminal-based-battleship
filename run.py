import random
import os
# Welcome to another battleship game!
# This is a simple terminal based game based on the two tutorials:
# https://llego.dev/posts/how-code-simple-battleship-game-python/
# and
# https://www.pyshine.com/Make-a-battleship-game/

# BATTLESHIP

# Creates the game board


def create_board(size):
    return [['~'] * size for _ in range(size)]


# Prints the board in the terminal

def print_board(board):
    i = 1
    print(' ', 1, 2, 3, 4, 5)
    for row in board:

        print(i, ' '.join(row))
        i = i + 1
    print()

# Ship placement based on randomization


def place_ships(board, num_ships):
    ships = 0
    while ships < num_ships:
        x, y = random.randint(0, len(board) - 1), \
            random.randint(0, len(board) - 1)
        if board[x][y] == '~':
            board[x][y] = 'S'
            ships += 1


# User input and input validator

def get_user_guess(board):
    while True:
        guess = input("Enter your guess (row and column, e.g., 2 3): ").split()
        print()
        if len(guess) == 2 and guess[0].isdigit() and guess[1].isdigit() \
                and int(guess[0]) < (board+1) and int(guess[1]) < (board+1):
            os.system('cls' if os.name == 'nt' else 'clear')
            return int(guess[0])-1, int(guess[1])-1
        else:
            print("Invalid input")
            print("Please enter two numbers separated by a space.")

# Enemy move based on randomizaton


def get_enemy_guess(board):
    guess = random.randint(0, board - 1), random.randint(0, board - 1)
    return int(guess[0]), int(guess[1])

# Sets up the players and enemy boards for the game


def setup_game(board_size, num_ships, showenemy):
    player_board = create_board(board_size)
    enemy_board = create_board(board_size)

    print("Your ships have been placed:")
    place_ships(player_board, num_ships)
    print_board(player_board)

    print("The enemy has placed their ships:")
    print("---")
    place_ships(enemy_board, num_ships)

    if showenemy is True:
        print_board(enemy_board)

    return player_board, enemy_board

# The main game run function


def play_game():
    print("Welcome to Battleship! A game of pure luck... Good luck!")
    print("Your goal is to sink all of your opponent's fleet of ships") 
    print("before they sink yours!")
    print("Each player takes turns guessing the coordinates of the opponent's ships.")
    print("in this version, you are playing against a computer that will do its")
    print("very best to destroy you and it is up to you to destroy it first!")
    print("The first player to sink all of the opponent's ships wins.")
    print("'~' are unknown playing fields, 'O' are guessed and missed field")
    print("and 'X' are guessed and hit fields!")
    


    # Question if you wish to see the location of enemy ships or not
    # (Used for testing)
    answer = False
    showenemy = False
    while answer is False:
        show = input("Would you like to see the enemy ship locations? \
                    [Used for testing] y/n")
        if show is "y":
            os.system('cls' if os.name == 'nt' else 'clear')
            showenemy = True
            print("Please note the enemy ship placements before proceeding!")
            break
        elif show == "n":
            break
        else:
            answer = False

    board_size = 5
    num_ships = 3
    player_board, enemy_board = setup_game(board_size, num_ships, showenemy)
    player_guesses = create_board(board_size)
    enemy_guesses = create_board(board_size)

    player_ships = num_ships
    enemy_ships = num_ships
    turn = 0

    while player_ships > 0 and enemy_ships > 0:
        if turn % 2 is 0:
            print("Your turn")
            print_board(player_guesses)
            guess = get_user_guess(board_size)
            if enemy_board[guess[0]][guess[1]] == 'S':
                print("You hit!")
                player_guesses[guess[0]][guess[1]] = 'X'
                enemy_board[guess[0]][guess[1]] = 'X'
                enemy_ships -= 1
            else:
                print("You missed.")
                print("---")
                player_guesses[guess[0]][guess[1]] = 'O'
        else:
            print("Enemys turn")
            print_board(enemy_guesses)
            guess = get_enemy_guess(board_size)
            if player_board[guess[0]][guess[1]] == 'S':
                print("Enemy has hit you!")
                enemy_guesses[guess[0]][guess[1]] = 'X'
                player_board[guess[0]][guess[1]] = 'X'
                player_ships -= 1
            else:
                print("Enemy Missed!")
                print("---")
                enemy_guesses[guess[0]][guess[1]] = 'O'

        turn += 1

    if player_ships is 0:
        print("Enemy wins!")
    else:
        print("Congrats! you have sank all the enemy ships.")
    


if __name__ == "__main__":
   while True:  # Re-run program
    play_game()

    while True:  # Validate user input
        answer = input('Would you like to play again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print("invalid input.")

    if answer == 'y':
        continue
    else:
        print("Goodbye")
        print(chr(27) + "[2J")
        break
