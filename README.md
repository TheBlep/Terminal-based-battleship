# Battleship
![Game Mockup](assets/images/mockup.png)

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
In this version, you are playing against a computer that will do its very best to destroy you and it is up to you to destroy it first!

To play the game:
1. Start the game by running the [Heroku](https://terminal-based-battleship-ad2683f69f33.herokuapp.com/) app.
2. Choose wether you wish to see the enemy ship placement by entering **y** for yes or **n** for no.
2. Enter the coordinates for your guesses when prompted.
3. The game will indicate whether you have hit or missed a ship.
4. Continue guessing until all ships are sunk!

## Features

### Existing Features
- **Interactive Command Line Interface:** The game is played through the terminal.
  ![Terminal play screen](assets/images/welcome-terminal2.png)
- **Random Ship Placement:** Ships are placed randomly on the board at the start of each game.

  ![Ship placement](assets/images/ship-placement.png)
- **Turn-based Gameplay:** Players take turns to guess the coordinates of enemy ships.

  ![Player turns](assets/images/turn-based.png)
- **Victory Message:** The game announces the winner when all ships of one player are sunk.

  ![Victory message](assets/images/victory.png)
  - **Colorama:** Throughout the player will experiance a bit more than the normal black and white termainl text with colors inported with colorama. This adds some variation to text and not only adds ot the interesting factor but also increases contrast of important messages and clarifies positive or negative results.

### Future Features
- **Multiplayer Mode:** Allowing two players to play remotely.
- **Enhanced AI:** Improving the computer's strategy for choosing guesses, such as implementing known battlefield scanning patterns or even a basic neural network.
- **Graphical Interface:** Adding a GUI for a more engaging experience.
- **Different size ships** Adding different size ships to allow variation and add a bit more stratagy to the game.
- **Player ship placement** Allow the player to decide their ship placement and orentation (assuming different size ships).
- **Restart game from play screen** Allow the player to restart the game, for exaimple by pressing r instead of giving a



## Data Model
The data model for Battleship includes:
- **Grids:** A 10x10 grid representing the game board; "~" representing unknown waters, "S" representing ships, "X" representing hit marks, "O" representing guessed and missed marks.
- **Guesses:** Each time the player or computer guesses, the grid is updated ot show this change and its result.

## Testing

False input testing for all game inputs:
- A letter (not the one requested) "a"
- Multiple letters "abc"
- A single number "1"
- Multiple numbers "123"
- An empty ENTER with no input
- Only spaces          
- Special characters ? ! @ etc

### Bugs

#### Solved Bugs
- **Bug:** Game crash when inputting invalid coordinates.
    - **Solution:** Added input validation to handle incorrect inputs.
- **Bug:** shortening of long lines caused breakage.
    - **Solution:** Added correct syntax "\" to lines to fix the problem.
- **Bug:** the input of 0 0 was possible due to no lower limit.
    - **Solution:** Added check that input is greated than 0.

#### Remaining Bugs
- **Bug:** Player and computer are able to guess a single tile more than once, 
    waisting a turn.  
    - **Status:** This could be solved with a tracker function, preventing duplicate inputs for a single game.

### Validator
The code has been validated using the following tools:
- **PEP8:** Ensuring Python code style guidelines are met.

![PEP8 verification](assets/images/ci-val.png)

- **Heroku Validator:** Ensuring the application is correctly deployed and running on Heroku.

## Deployment
The game was deployed using the Heroku app hosting service:
- Steps for deployment
    - Fork or clone the [respository](https://github.com/TheBlep/Terminal-based-battleship)
    - Create a new Heroku app
    - Set the buildpacks (under settings) to 'Python' and 'NodeJS'. Where Python is **above** NodeJS
    - Link the Heroku app to the repository
    - Click on **Deploy**
- Active deployment
    - Another option is to use the active Heroku deplyoment [here](https://terminal-based-battleship-ad2683f69f33.herokuapp.com/)
- Local deployment
    - Fork or clone the [respository](https://github.com/TheBlep/Terminal-based-battleship)
    - Open the file in your favorate IDE
    - Run the run.py in a python terminal
    - Enjoy!

## Credits
- **Developer:** TheBlep
- **Inspiration:** The classic Battleship game
- **Resources:** Python documentation, Heroku deployment guides, W3C, and two tutorials:
    https://llego.dev/posts/how-code-simple-battleship-game-python/ and \
    https://www.pyshine.com/Make-a-battleship-game/