# Battleship
![Game Mockup](<screenshot>)

## Table of Contents
1. [How to Play](#how-to-play)
2. [Features](#features)
   - [Existing Features](#existing-features)
   - [Future Features](#future-features)
3. [Data Model](#data-model)
4. [Testing](#testing)
   - [Bugs](#bugs)
     - [Solved Bugs](#solved-bugs)
     - [Remaining Bugs](#remaining-bugs)
   - [Validator](#validator)
5. [Development](#development)
6. [Credits](#credits)

## How to Play
Battleship is a classic strategy game where you try to sink your opponent's fleet of ships before they sink yours. Each player takes turns guessing the coordinates of the opponent's ships. The first player to sink all of the opponent's ships wins.

To play the game:
1. Start the game by running the `run.py` file.
2. Enter the coordinates for your guesses when prompted.
3. The game will indicate whether you have hit or missed a ship.
4. Continue guessing until all ships are sunk.

## Features

### Existing Features
- **Interactive Command Line Interface:** The game is played through the terminal.
  ![CLI Screenshot](<screenshot>)
- **Random Ship Placement:** Ships are placed randomly on the board at the start of each game.
- **Turn-based Gameplay:** Players take turns to guess the coordinates of enemy ships.
- **Victory Message:** The game announces the winner when all ships of one player are sunk.

### Future Features
- **Multiplayer Mode:** Allowing two players to play remotely.
- **Enhanced AI:** Improving the computer's strategy for choosing guesses.
- **Graphical Interface:** Adding a GUI for a more engaging experience.

## Data Model
The data model for Battleship includes:
- **Grid:** A 10x10 grid representing the game board.
- **Ships:** Different types of ships with varying lengths.
- **Guesses:** Coordinates where the player has guessed.

## Testing

### Bugs

#### Solved Bugs
- **Bug 1:** Incorrect ship placement causing overlap.
  - **Solution:** Implemented a check to ensure ships do not overlap.
- **Bug 2:** Game crash when inputting invalid coordinates.
  - **Solution:** Added input validation to handle incorrect inputs.

#### Remaining Bugs
- **Bug 3:** Occasionally, the game does not recognize a hit.
  - **Status:** Under investigation.

### Validator
The code has been validated using the following tools:
- **PEP8:** Ensuring Python code style guidelines are met.
- **Heroku Validator:** Ensuring the application is correctly deployed and running on Heroku.

## Development
The development process included:
1. **Planning:** Outlining the game logic and features.
2. **Implementation:** Coding the game in Python.
3. **Testing:** Identifying and fixing bugs.
4. **Deployment:** Hosting the game on Heroku.

## Credits
- **Developer:** TheBlep
- **Inspiration:** Classic Battleship game
- **Resources:** Python documentation, Heroku deployment guides