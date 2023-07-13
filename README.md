# Battleships Game

This is a simple application of the Battleships game in the Python terminal. The game is about taking guesses in turns between the player and the computer to find and destroy each other's battleships. When the maximum number of turns is reached or all the ships of either player are destroyed, the game ends.

## Game Board

The game board is represented by a grid of rounded-corner squares. Squares can contain a ship or be empty. The board is displayed using ASCII characters, with "▢" representing empty squares and "O" representing the ships placed for the player automatically and randomly when the game starts.

## Features

### Existing Features
- Random board creation
    - Automatically and randomly placed ships on both the computer and the players' boards.
    - The computer's ships are not visible to the player and vice versa.

![initial screen]()

- Play against the computer
- Takes user input
- Keeps scores (still needs to be implemented)

![turns]()

- Input validation and error-checking
    - You cannot enter the same coordinates twice
    - You cannot enter coordinates higher than the size of the grid
    - You must enter numbers

![validation]()

- Data maintained in class instances

### Possible Future Features
- Allow player to select the board size and the number of ships
- Allow player to place ships on the board by themselves
- Have different ship sizes

## Data Model
I used a Board class as my model. It creates two class instances, one for the player and one for the computer boards.

The Board class stores the board size, the amount of ships, the placement of the ships, the guesses against that board, the board type and the player's name. 

The class also has methods to assist in the gameplay such as a "print" method to print out the boards, a "guess" method to add the guess to the board and an add_ships method to add the ships to the board.

## Game Flow

1. The player and computer take turns guessing the positions of the battleships on the opponent's board.
2. The player enters the row and column coordinates for their guess.
3. The computer generates random coordinates for its guess.
4. The game checks if the guess is a hit or a miss.
5. The board is updated with "X" on each board to reflect the guess.
6. The game ends when all ships of either participant are destroyed or the maximum number of turns is reached.




### Code Structure

The code consists of the following components:

- `Board` class: Represents the game board and provides methods to print the board, add ships, and handle guesses.
- `valid_places` function: Checks if the provided coordinates are valid within the bounds of the game board.
- `fill_board` function: Fills the game board with ships by generating random coordinates and checking for validity.
- `take_guess` function: Handles the player's guess input by prompting for row and column coordinates, validating the inputs, and updating the board.
- `computer_guess` function: Generates random coordinates for the computer's guess and updates the board accordingly.
- `start_game` function: Initializes the game, prints the initial board state, and handles the game flow until a win condition or maximum turns are reached.
- `run_game` function: Entry point of the game, sets up the game parameters, creates the player and computer boards, and starts the game.

### Running the Game

To play the game, simply execute the code. The game will prompt you for your name and display the initial game board. Enter the row and column coordinates for your guess when prompted, and the game will indicate whether it's a hit or a miss. The computer will then take its turn. The game continues until a win condition or the maximum number of turns is reached.

Enjoy the Battleships game!