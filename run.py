# Import math random (For generating random numbers)
import random
# Import operating system interaction (For clearing terminal)
import os
# Import colorma module (For terminal colors)
from colorama import init, Fore, Back, Style
# For direct program termination
import sys

# Welcome to another battleship game!
# This is a simple terminal based game based on the two tutorials:
# https://llego.dev/posts/how-code-simple-battleship-game-python/
# and
# https://www.pyshine.com/Make-a-battleship-game/

# BATTLESHIP!


def create_board(size):
    """Creates the game board"""
    return [['~'] * size for _ in range(size)]


def print_board(board):
    """Prints the board in the terminal"""
    i = 1
    print(Style.RESET_ALL + ' ', "1", "2", "3", "4", "5")
    for row in board:

        print(i, ' '.join(row))
        i = i + 1
    print()


def place_ships(board, num_ships):
    """Ship placement based on randomization"""
    ships = 0
    while ships < num_ships:
        x, y = random.randint(0, len(board) - 1), \
            random.randint(0, len(board) - 1)
        if board[x][y] == '~':
            board[x][y] = 'S'
            ships += 1


def get_user_guess(board):
    """User input and input validator"""
    while True:
        guess = input(\
            "Enter your guess (row and column, e.g., 2 3 or 'q' to quite): ").split()
        print()
        if len(guess) == 2 and guess[0].isdigit() and guess[1].isdigit() \
                and int(guess[0]) < (board+1) and int(guess[1]) < (board+1) \
                and int(guess[0]) > (0) and int(guess[1]) > (0):
            # Used to clear terminal on most devices.
            os.system('cls' if os.name == 'nt' else 'clear')
            return int(guess[0])-1, int(guess[1])-1
        elif len(guess) == 1 and guess[0] == "q":
            sys.exit()
            break
        else:
            print(Fore.RED + "Invalid input")
            print(Style.RESET_ALL + \
                "Please enter two numbers separated by a space.")


def get_enemy_guess(board):
    """Enemy move based on randomizaton"""
    guess = random.randint(0, board - 1), random.randint(0, board - 1)
    return int(guess[0]), int(guess[1])


def setup_game(board_size, num_ships, showenemy):
    """Sets up the players and enemy boards for the game"""
    player_board = create_board(board_size)
    enemy_board = create_board(board_size)

    print(Style.RESET_ALL + "Your ships have been placed:")
    place_ships(player_board, num_ships)
    print_board(player_board)

    print("The enemy has placed their ships:")
    place_ships(enemy_board, num_ships)

    if showenemy is True:
        print_board(enemy_board)

    return player_board, enemy_board


def play_game():
    """The main game run function"""
    # Used to clear terminal on most devices.
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to Battleship! A game of pure luck... Good luck!")
    print("Your goal is to sink all of your opponent's fleet of ships")
    print("before they sink yours!")
    print("Each player takes turns guessing the coordinates of the")
    print("opponent's ships. in this version, you are playing against a")
    print("computer that will do its very best to destroy you and it is")
    print("up to you to destroy it first!")
    print("The first player to sink all of the opponent's ships wins.")
    print("'~' are unknown playing fields, 'O' are guessed and missed field")
    print("and 'X' are guessed and hit fields!")

    # Question if you wish to see the location of enemy ships or not
    # (Used for testing)
    answer = False
    showenemy = False
    while answer is False:
        show = input(Fore.YELLOW + \
            "Would you like to see the enemy ship locations? \
                [Used for testing] y/n")
        if show is "y":
            os.system('cls' if os.name == 'nt' else 'clear')
            showenemy = True
            print(Fore.RED + "Please note the enemy ship placements \
            before proceeding!")
            break
        elif show == "n":
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + "Invalid input")
            print(Style.RESET_ALL + "Please enter a 'y' or an 'n'.")

    board_size = 5
    num_ships = 3
    player_board, enemy_board = setup_game(board_size, num_ships, showenemy)
    player_guesses = create_board(board_size)
    enemy_guesses = create_board(board_size)

    player_ships = num_ships
    enemy_ships = num_ships
    turn = 0

    # Request, verify, print and save turn input

    while player_ships > 0 and enemy_ships > 0:
        if turn % 2 is 0:

            # Could be made into a seperate function
            # Player and enemy input respectivly

            print(Fore.GREEN + "Your turn!")
            print(' ')
            print(Style.RESET_ALL + "Your guesses so far...")
            print_board(player_guesses)
            guess = get_user_guess(board_size)
            if enemy_board[guess[0]][guess[1]] == 'S':
                print(Fore.RED + "You hit!")
                player_guesses[guess[0]][guess[1]] = 'X'
                enemy_board[guess[0]][guess[1]] = 'X'
                enemy_ships -= 1
            else:
                print(Fore.RED + "You missed.")
                print("---")
                player_guesses[guess[0]][guess[1]] = 'O'
        else:
            # Computer "Enemy" input
            print(Fore.RED + "Enemys turn")
            print(' ')
            print(Style.RESET_ALL + "Enemy guesses so far...")
            print_board(enemy_guesses)
            guess = get_enemy_guess(board_size)
            if player_board[guess[0]][guess[1]] == 'S':
                print(Fore.RED + "Enemy has hit you!")
                enemy_guesses[guess[0]][guess[1]] = 'X'
                player_board[guess[0]][guess[1]] = 'X'
                player_ships -= 1
            else:
                print(Style.RESET_ALL + "Enemy Missed!")
                print("---")
                enemy_guesses[guess[0]][guess[1]] = 'O'

        turn += 1
    # Decides endgame message based on who won
    if player_ships is 0:
        print(Fore-RED + "Enemy wins!")
    else:
        print(Fore.GREEN + "Congrats! you have sank all the enemy ships!")


# """Main game loop"""
# if __name__ == "__main__":
#     while True:  # Re-run program
#         play_game()

#     while True:  # Validate user input
#         answer = input(Style.RESET_ALL + 'Would you like to play again?\
#         (y/n): ')
#         if answer in ('y', 'n'):
#             break
#         print(Fore.RED + "invalid input.")

#     if answer == 'y':
#         continue
#     else:
#         print(Style.RESET_ALL + "Goodbye")
#         print(chr(27) + "[2J")
#         break

"""Main game loop"""
if __name__ == "__main__":
    while True:  # Re-run program
        play_game()

        while True:  # Validate user input
            answer = input(Style.RESET_ALL + 'Would you like to play again? (y/n): ')
            if answer in ('y', 'n'):
                break
            print(Fore.RED + "invalid input.")

        if answer == 'y':
            continue
        else:
            print(Style.RESET_ALL + "Goodbye")
            print(chr(27) + "[2J")
            break
