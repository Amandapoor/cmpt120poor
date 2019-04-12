# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Amanda Poor
# Created: 2019-08-04


symbol = [ " ", "x", "o" ]

def printRow(row):

    output = "|"
    for i in range(3):
        output = output + " " + symbol[row[i]] + " |"
    print(output)
   

def printBoard(board):

    print("+-----------+")
    
    for i in range(3):
        printRow(board[i])
        print("+-----------+")
        

    
def players(player1,player2):
    player1 == "x"
    player2 == "o"
    


def markBoard(board, row, col, player):
    
    if board[row][col] == 0:
        board[row][col] = player
    
    else:
        print("Filled location. Pick another one.")
        
   

def getPlayerMove():
    
    row = int(input("Enter a row for the play (1-3):")) 
    col = int(input("Enter a column for the play (1-3):"))
    return (row - 1, col - 1)


    

def hasBlanks(board):
    for row in board:
        for col in row:
            if col == 0:
                return True

    return False

def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]

    player = 1
    
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1
    printBoard(board)
    

    
main()
