# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 7 Activity 3
# Date:         10/8/2020
# thank group member for doing this. 

print('This program sets up a chess board and allows people to make moves on the chess board.')


# create 2d list of the chessboard
chess_board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'], 
               ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
               ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]


# print the chess board 
for i in range (len(chess_board)):
    print()
    for j in range (len(chess_board)):
        print(chess_board[i][j], end = ' ')
print()        
        
# variables:
# keeps track of how many pieces are left on the board and which piece is being moved
piece_count = 32
piece = ''


# program will run until one piece is left on the board
while (piece_count != 1):
    # ask user for coordinate of the piece
    row = int(input('Please enter the row number of the piece you would like to move. (0-7): '))
    col = int(input('Please enter the column number of the piece you would like to move. (0-7): '))


    # piece holds value of the inputed coordinate - change old coordinate to a .
    piece = chess_board[row][col]
    chess_board[row][col] = '.'
    
            
    # check to make sure that the coordinates has a piece and is not empty
    if (piece == '.'):
        print('Error: space provided has no piece.')
        break
    
    # if coordinates have a piece, move it to new coordinates
    elif (piece != '.'):
        # ask user where they would like to move the piece
        row_move = int(input('Please enter the row number of where ' 
                             'you would like to move the piece. (0-7): '))
        col_move = int(input('Please enter the column number of where ' 
                             'you would like to move the piece. (0-7): '))
        
        # check to see if coordinate moved to has a piece in it - if yes remove one from piece_count
        if (chess_board[row_move][col_move] != '.'):
            piece_count -= 1
        # assign new coordinates the value of piece
        chess_board[row_move][col_move] = piece
       
        
        # print chess board after changes
        for i in range (len(chess_board)):
            print()
            for j in range (len(chess_board)):
                print(chess_board[i][j], end = ' ')
        print()

