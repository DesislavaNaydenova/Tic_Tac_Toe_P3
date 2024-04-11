import random

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
            print("", board[x][y], end=" |")
    print("\n+---+---+---+")

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
    return 
        # rows
        (board[0][0] == board[0][1] == board[0][2] == player) or\
        (board[1][0] == board[1][1] == board[1][2] == player) or\
        (board[2][0] == board[2][1] == board[2][2] == player) or\
        #columns
        (board[0][0] == board[1][0] == board[2][0] == player) or\
        (board[0][1] == board[1][1] == board[2][1] == player) or\
        (board[0][2] == board[1][2] == board[2][2] == player) or\
        #diagonals
        (board[0][0] == board[1][1] == board[2][2] == player) or\
        (board[0][2] == board[1][1] == board[2][0] == player)

#put the player's mark on the choosen position
def insertMark(mark, move):
     row = (move-1) // 3
    col = (move-1) % 3
    board[row][col] == mark

#player turn
def playerMove():
    run = True
    while run:
        move = input("Select a positin (1-9) to place your mark \"X\": ")
        if move = int(move):
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

#checking for win

#computer turn

#checking for win

#main function
def main():
    printBoard()

#ask if the player wants to play again

main()

