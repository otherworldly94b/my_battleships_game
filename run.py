from random import randint

# Create the game board
# Initial code from CI sample video
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


    def print(self):
        """
        Function to print the board
        """
        for row in self.board:
            print(" ".join(row))


    def guess(self, x, y):
        """
        Function for player guess
        """
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "It's a Hit"
        else:
            return "It's a Miss"
    

    def add_ship(self, x, y, type="computer"):
        """
        Function for computer guess
        """
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


def fill_board(board):
    """
    Function to place the ships on the board
    """
    ship_row = randint(0, 5)
    ship_col = randint(0, 5)
    return ship_row, ship_col

def take_guess(board):
    """
    Handles the player's guess input
    """
    x = int(input("Enter row position (0 to 4): "))
    y = int(input("Enter column position (0 to 4): "))
    result = board.guess(x, y)
    print(result)


def start_game(computer_board, player_board):
    print('============= PLAYER ===============')
    player_board.print()
    print('====================================')
    print('\n')
    print('=========== COMPUTER ===============')
    computer_board.print()
    print('====================================')
    while True:
        print("Player's Turn")
        take_guess(computer_board)
        computer_board.print()
        print("")

        # Confirm if the player has won
        if scores["computer"] == player_board.am_ships:
            print("Amazing! You won!")
            break

        

def run_game():
    """
    Starts a new game. Creates the board size, adds the number of ships, 
    resets the scores and updates the boards.
    """

    size = 5
    am_ships = 4 
    scores["player"] = 0
    scores["computer"] = 0 
    print("_" * 25)
    print("BATTLESHIPS UNLEASHED!")
    print(f" Board Size: {size}. Ship availability: {am_ships}")
    print("row: 0, col: 0, found at the top left corner of the board")
    print("_" * 25)
    player_name = input("Please write your name, if you don't write anything then I will just call you Player: \n").strip()
    if player_name == '': 
        player_name = 'Player'
    print(f'OK, so hi there {player_name}')
    print("_" * 25)

    computer_board = Board(size, am_ships, "Computer", type="computer")
    player_board = Board(size, am_ships, player_name, type="player")
    sr = 0
    sc = 0
    for i in range(am_ships):
        sr = fill_board(player_board)
        sc = fill_board(computer_board)
​
    print(sr)
    print(sc)
​
    start_game(computer_board, player_board)

run_game()