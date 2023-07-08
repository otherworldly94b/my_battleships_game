from random import randint

# Create the game board
# Code from CI sample video
class Board:
    """
    Creates the main board. Sets the size and the number 
    of ships allowed and the player's name.
    There are methods that print the board, add the ships
    and the guess on the board
    """
    def __init__(self, size, am_ships, name, type):
        self.size = size
        self.board = [["▢" for x in range(size)] for y in range(size)]
        self.am_ships = am_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    # Function to print the board
    def print(self):
        for row in self.board:
            print(" ".join(row))

    # Function for player and computer guess
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "It's a Hit"
        else:
            return "It's a Miss"
    
    