# Battleships Game

This is a simple application of the Battleships game in the Python terminal. The game allows the player to guess the positions of the ships on the game board and compete against the computer. The player and computer take turns guessing the positions until all ships are destroyed or the maximum number of turns is reached.

## Game Board

The game board is represented by a grid of squares. Each square can be empty or contain a ship. The board is displayed using ASCII characters, with "▢" representing empty squares and "O" representing ships placed by the player.

## Game Flow

1. The player and computer take turns guessing the positions on the opponent's board.
2. The player enters the row and column coordinates for their guess.
3. The computer generates random coordinates for its guess.
4. The game checks if the guess is a hit or a miss.
5. The board is updated to reflect the guess.
6. The game continues until all ships of either the player or the computer are destroyed or the maximum number of turns is reached.

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