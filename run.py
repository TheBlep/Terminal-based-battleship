# Its a battleship game! woo!

# Setting up grid constants
GRID_SIZE = 10
SHIPS = {'Destroyer': 2, 'Submarine': 3, 'Battleship': 4}

# Playing feilds
player_grid = [['~'] * GRID_SIZE for _ in range(GRID_SIZE)]
enemy_grid = [['~'] * GRID_SIZE for _ in range(GRID_SIZE)]

# Placing ships randomly
import random
def random_row():
    return random.randint(0,GRID_SIZE -1)

def random_col():
    return random.randint(0,GRID_SIZE -1)

#def place_ships(ships, size, grid)
