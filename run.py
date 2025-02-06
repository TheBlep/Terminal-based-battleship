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

# Player turn logic
def player_move():

    print("Enter row and column to obliterate without remorse")

    row, col = input().split()
    row, col = int(row), int(col)

    mark = enemy_grid[row][col]

    if mark == 'X' or mark == '.':
        print ("Stop wasting ammunition, noob")
        return

    if mark == '~':
        print ("Miss........ You are not very good at this, try again")
        enemy_grid[row][col] = '.'
    
    else:
        print ("Hit! May they feel our wrath...")
        enemy_grid[row][col] = 'X'

# Enemy turn logic

def enemy_move():

    row = random_row()
    col = random_col()

    mark = player_grid[row][col]

    if mark == 'X' or mark == '.':
        return
    if mark == '~':
        print ("We have once again evaded their inferior guns")
        player_grid[row][col] = '.'
    else:
        print("We have taken damage. May they feel hellfire")
        player_grid[row][col] = 'X'

# Main game loop

while True:
    player_move()
    print_grid(enemy_grid)

    enemy_move()
    print_grid(player_grid)

# Checking for a win

if all_ships_sunk(enemy_grid):
    print("We have successfully commited genocide")
    break

# Checking if valid player input

try:
    row, col = input("Enter row and colunm: ").split()
    row, col = int(row), int(col)
except ValueError:
    print("Please enter valid coordinates, Commander")
    continue

# Exiting game

action = input("Your move: ")
if action.lower() == 'quit':
    print("You have retired [Quit the game]")
    break
