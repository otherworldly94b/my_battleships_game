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
            pass
        else:
            self.ships.append((x, y))
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
        return False
    else:
        return True


def fill_board(board):
    """
    Fills the board with how many ships are available and
    checks for correct coordinates
    """
    for _ in range(board.am_ships):
        while True:
            x = random_point(board.size)
            y = random_point(board.size)

            if valid_places(board.size, x, y, board.ships):
                board.add_ship(x, y)
                break


def take_guess(board):
    """
    Handles the player's guess input.
    There are 4 paths:
    1. Use valid coordinates
    2. Use "q" to quit
    3. Use coordinates that have used before and receive an error message
    4. Use invalid coordinates and receive an error message.
    """
    while True:
        xrow_input = input("Enter row position (0 to 4) or 'q' to quit: \n")

        if xrow_input.lower() == 'q':
            print("Quitting the game...")
            exit()

        if not xrow_input.isdigit():
            print("Please provide a valid integer coordinate or 'q' to quit.")
            continue

        ycol_input = input("Enter column position (0 to 4) or 'q' to quit: \n")

        if ycol_input.lower() == 'q':
            print("Quitting the game...")
            exit()

        if not ycol_input.isdigit():
            print("Please provide a valid integer coordinate or 'q' to quit.")
            continue

        x = int(xrow_input)
        y = int(ycol_input)

        if not valid_places(board.size, x, y, board.guesses):
            print("Try valid coordinates or ones you have not used before")
        else:
            result = board.guess(x, y)
            print(result)
            break


def computer_guess(player_board):
    while True:
        x = random_point(player_board.size)
        y = random_point(player_board.size)

        if (x, y) not in player_board.guesses:
            break

    result = player_board.guess(x, y)
    print(f"Computer guessed: row {x}, column {y}")
    print(result)

    if result == "It's a Hit":
        scores["computer"] += 1


def start_game(computer_board, player_board):
    print('=============== PLAYER ===============')
    player_board.print()
    print('====================================')
    print('\n')
    print('=============== COMPUTER =============')
    computer_board.print()
    print('====================================')

    max_turns = 25  # Maximum number of turns equivalent to all squares
    turn = 0  # Turn counter

    while True:
        print("Player's Turn")
        take_guess(computer_board)
        computer_board.print()
        print("")

        # Check if the game is over after each guess
        if scores["computer"] == player_board.am_ships or scores["player"] == computer_board.am_ships:
            break

        # Confirm if the computer has won
        if scores["player"] == computer_board.am_ships:
            print("Oops! All your ships are destroyed! Computer won!")
            break

        turn += 1
        if turn >= max_turns:
            print("Maximum number of turns reached. Game over!")
            break

        print("Computer's Turn")
        computer_guess(player_board)
        player_board.print()
        print("")

        # Check if the game is over after each guess
        if scores["computer"] == player_board.am_ships or scores["player"] == computer_board.am_ships:
            print("Game Over! All ships on a board have been destroyed")
            break


# Initial code from CI sample video


def run_game():
    """
    Starts a new game. Creates the board size, adds the number of ships,
    resets the scores and updates the boards.
    """

    size = 5
    am_ships = 4
    scores["player"] = 0
    scores["computer"] = 0
    print("_" * 45)
    print("BATTLESHIPS UNLEASHED!")
    print(f"Board Size: {size}. Ship availability: {am_ships}")
    print("row: 0, col: 0, found at the top left corner of the board")
    print("Ships are automatically and randomly placed for both the players")
    print("_" * 45)
    player_name = input("Type your name, or just be called Player: \n").strip()
    if player_name == '':
        player_name = 'Player'
    print(f'OK, so hi there {player_name}')
    print("_" * 45)

    computer_board = Board(size, am_ships, "Computer", type="computer")
    player_board = Board(size, am_ships, player_name, type="player")

    sr = 0
    sc = 0
    for i in range(am_ships):
        sr = fill_board(player_board)
        sc = fill_board(computer_board)

    start_game(computer_board, player_board)


scores = {"player": 0, "computer": 0}
run_game()
