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

def place_ships(ships, size, grid):
    
    # Randomly generate row and col index for bow of ship.
    row = random_row()
    col = random_col()

    # Randomly chooses ship orientation
    is_vertical = random.choice([True, False])

    if is_vertical:
        if row + size > GRID_SIZE:
            return False

        for i in range(size):
            grid[row+i][col] = ship[0]

    else:
        if col +size > GRID_SIZE:
            return False
            
        for i in range(size):
            grid[row][col+i] = ship[0]

    return True

# Populate the grid
# Repeatedly call until each ship fits

for ship, size in ships.item():
    while True:
        placed = place_ship(ship, size, grid)
        if placed:
            break

