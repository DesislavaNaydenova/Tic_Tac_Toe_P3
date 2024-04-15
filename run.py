import random

# ANSI color escape codes
GREEN = '\033[32m'
RED = '\033[91m'
RESET = '\033[0m'

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to my TicTacToe Game!")
print("          Enjoy!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#creating the board

cells = [1,2,3,4,5,6,7,8,9]
board = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
columns = 3

def printBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end = "")
        for y in range(columns):
            if board[x][y] == "X":
                print("", f"{GREEN}X{RESET}", end=" |")
            elif board[x][y] == "O":
                print("", f"{RED}O{RESET}" , end=" |")
            else:
                print("", board[x][y], end=" |")
    print("\n+---+---+---+")

#resets the board to enable a new game
def resetBoard():
    global board
    board = [[1,2,3], [4,5,6], [7,8,9]]

#update the board after every turn
def updateArray(num, turn):
    #calculate location on board based on position num
    row = (num-1) // 3
    col = (num-1) % 3
    board[row][col] = turn

#checking if the selected position is free
def posFree(move):
    row = (move-1) // 3
    col = (move-1) % 3
    return board[row][col] == move

#checking for winn
def checkWinner(board, player):
    return (board[0][0] == board[0][1] == board[0][2]) or\
        (board[1][0] == board[1][1] == board[1][2]) or\
        (board[2][0] == board[2][1] == board[2][2]) or\
        (board[0][0] == board[1][0] == board[2][0]) or\
        (board[0][1] == board[1][1] == board[2][1]) or\
        (board[0][2] == board[1][2] == board[2][2]) or\
        (board[0][0] == board[1][1] == board[2][2]) or\
        (board[0][2] == board[1][1] == board[2][0])

#put the player's mark on the choosen position
def insertMark(mark, move):
    row = (move-1) // 3
    col = (move-1) % 3
    board[row][col] = mark

#player turn
def playerMove():
    run = True
    while run:
        move = input("Select a positin (1-9) to place your mark \"X\": \n")
        if move.isdigit():
            move= int(move)
            if move > 0 and move <10:
                if posFree(move):
                    run = False
                    insertMark("X", move)
                else:
                    print("This position is already been choosen!")
            else:
                print("Coose a number in the range between 1 and 9!")
        else:
            print("Please type a number!")



#computer turn
def computerMove():
    possibleMoves = [x for x in range(1, 10) if isinstance(board[(x-1)//3][(x-1)%3], int)]
    if possibleMoves:
        move = random.choice(possibleMoves)
        return move
    else:
        return None

#main function
def main():
    printBoard()
    while True:
        playerMove()
        printBoard()
        if checkWinner(board, "X"):
            print("Congratulations! You win!")
            break
        comp_move = computerMove()
        if comp_move is not None:
            insertMark("O", comp_move)
            print("The computer has made its move.")
        else:
            print("No more moves available. It's a tie!")
            break
        printBoard()
        if checkWinner(board, "O"):
            print("Sorry! Computer wins!")
            break
    # Ask if the player wants to play again
    while True:
        playAgain = input("Do you want to play again? (y/n): \n")
        if playAgain.lower() == "y":
            resetBoard()
            main()
        elif playAgain.lower() == "n":
            print("Thank you for playing! See you next time!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

main()

#ask if the player wants to play again







