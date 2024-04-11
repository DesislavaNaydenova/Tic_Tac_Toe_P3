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
#checking for winn

#player turn

#checking for win

#computer turn

#checking for win

#main function
def main():
    printBoard()

#ask if the player wants to play again

main()

