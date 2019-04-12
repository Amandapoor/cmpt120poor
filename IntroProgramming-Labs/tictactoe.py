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
        
    
    # print the top border
    # for each row in the board... # print the row
    # print the next border
    
player1 == " x "

def markBoard(board, row, col, player1):

    if board[row][col] == 0:
        board[row][col] = " x "
    
    else:
        print("Non empty location. Pick another one.")
        
player2 == " o "
def markBoard(board, row, col, player2):

    if board[row][col] == 0:
        board[row][col] = " o "
    
    else:
        print("Non empty location. Pick another one.")
    # check to see whether the desired square is blank # if so, set it to the player number

def getPlayerMove():
    
    row = int(input("Enter a row for the play (1-3):")) 
    col = int(input("Enter a column for the play (1-3):"))
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

        
 

    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove(player)
        markBoard(board,row,col,player)
        

    

   
    
main()
