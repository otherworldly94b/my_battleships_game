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

    # Function for player guess
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "It's a Hit"
        else:
            return "It's a Miss"
    
    # Function for computer guess
    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.am_ships:
            print("No more ships to be added")
        else:
            if self.type == "player":
                self.board[x][y] = "O"

def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)

def valid_places(size, x, y, guesses):
    """
    Checks the coordinates provided by the player.
    Checks if the coordinates are within the bounds of the game board.
    """
    if x < 0 or x >= size or y < 0 or y >= size or (x, y) in guesses:
        print("Please use valid coordinates or ones you have not used before")
    else:
        return True

