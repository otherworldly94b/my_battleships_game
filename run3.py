from random import randint

# Create the game board
board = []

for x in range(0, 5):
    board.append(["O"] * 5)

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to place the ships
def place_ship(board):
    ship_row = randint(0, len(board) - 1)
    ship_col = randint(0, len(board[0]) - 1)
    return ship_row, ship_col

# Start the game
print("Let's play Battleship!")
print_board(board)

ship_row, ship_col = place_ship(board)

# Game loop
for turn in range(4):
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if (turn == 3):
            print("Game Over")
        print_board(board)