"""This file displays a TicTacToe board on the terminal.

It lets the player make a move, calculates a random move
for the computerand displays the results of the game.
"""
import random

# ANSI color escape codes
GREEN = '\033[32m'
RED = '\033[91m'
RESET = '\033[0m'

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to my TicTacToe Game!")
print("          Enjoy!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# creating the board

cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
columns = 3


def print_board():
    """
    Ensure that the gameboard is visually represented in the terminal.

    Print "X" and "O" markers colored differently for better visibility.
    """
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(columns):
            if board[x][y] == "X":
                print("", f"{GREEN}X{RESET}", end=" |")
            elif board[x][y] == "O":
                print("", f"{RED}O{RESET}", end=" |")
            else:
                print("", board[x][y], end=" |")
    print("\n+---+---+---+")


def reset_board():
    """Reset the board to enable a new game."""
    global board
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def update_array(num, turn):
    """
    Update the board after every turn.

    Calculate location on board based on position num.
    """
    row = (num - 1) // 3
    col = (num - 1) % 3
    board[row][col] = turn


def pos_free(move):
    """Check if the selected position is free."""
    row = (move - 1) // 3
    col = (move - 1) % 3
    return board[row][col] == move


def check_winner(board, player):
    """Check for win."""
    return (board[0][0] == board[0][1] == board[0][2]) or\
        (board[1][0] == board[1][1] == board[1][2]) or\
        (board[2][0] == board[2][1] == board[2][2]) or\
        (board[0][0] == board[1][0] == board[2][0]) or\
        (board[0][1] == board[1][1] == board[2][1]) or\
        (board[0][2] == board[1][2] == board[2][2]) or\
        (board[0][0] == board[1][1] == board[2][2]) or\
        (board[0][2] == board[1][1] == board[2][0])


def insert_mark(mark, move):
    """Put the player's mark on the choosen position."""
    row = (move - 1) // 3
    col = (move - 1) % 3
    board[row][col] = mark


def player_move():
    """Handle the player move by getting the players input.

    Check it if it's an int. in range 1 - 9
    and if the choosen position is free.
    """
    run = True
    while run:
        move = input("Select a positin (1 - 9) to place your mark \"X\": \n")
        if move.isdigit():
            move = int(move)
            if move > 0 and move < 10:
                if pos_free(move):
                    run = False
                    insert_mark("X", move)
                else:
                    print("This position is already been choosen!")
            else:
                print("Coose a number in the range between 1 and 9!")
        else:
            print("Please type a number!")


def computer_move():
    """Ensure that the computer selects a valid, random move on the board."""
    possible_moves = [x for x in range(1, 10) if isinstance(
                    board[(x - 1) // 3][(x - 1) % 3], int)]
    if possible_moves:
        move = random.choice(possible_moves)
        return move
    else:
        return None


def main():
    """Arrange the game flow.

    Handle player and computer moves, checks for a winner,
    and manages the playAgain functionality.
    """
    print_board()
    while True:
        player_move()
        print_board()
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        comp_move = computer_move()
        if comp_move is not None:
            insert_mark("O", comp_move)
            print("The computer has made its move.")
        else:
            print("No more moves available. It's a tie!")
            break
        print_board()
        if check_winner(board, "O"):
            print("Sorry! Computer wins!")
            break
    # Ask if the player wants to play again
    while True:
        play_again = input("Do you want to play again? (y / n): \n")
        if play_again.lower() == "y":
            reset_board()
            main()
        elif play_again.lower() == "n":
            print("Thank you for playing! See you next time!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


main()
