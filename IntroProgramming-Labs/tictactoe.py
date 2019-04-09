# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Your Name Here
# Created: YYYY-MM-DD
symbol = [ " ", "x", "o" ]

def printRow(row):

    output = "|"
    for i in range(3):
        output = output + " " + symbol[row[i]] + " |"
        #if row[i]==1:
            #line = line + " x |"
        #elif row[i]==2:
            #line = line + " o |"
        #else:
            #line = line + "   |"
            
    print(line)
   

def printBoard(board):

    print("+-----------+")
    
    for i in range(3):
        printRow(board[i])
        print("+-----------+")
        
    
    # print the top border
    # for each row in the board... # print the row
    # print the next border
    

def markBoard(board, row, col, player):

    if board[row][col] == 0:
        board[row][col] = player
    else:
        print("Non empty location. Pick another one.")
    # check to see whether the desired square is blank # if so, set it to the player number
    pass
def getPlayerMove():
    row = int(input("Enter a row for the play (1-3):")
    col = int(input("Enter a column for the play (1-3):")
        return (row - 1, col - 1)
    
    
def hasBlanks(board):
    # for each row in the board...
    # for each square in the row...
    # check whether the square is blank
    # if so, return True
    return True # if no square is blank, return False

def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]

        
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn

    
main()
