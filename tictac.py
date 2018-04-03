import random

def display_board(board):    
    print ('   |  |')
    print (' ' + board[7] + ' | ' + board[8] + '| ' + board[9])
    print ('   |  |')
    print ('-----------')
    print ('   |  |')
    print (' ' + board[4] + ' | ' + board[5] + '| ' + board[6])
    print ('   |  |')
    print ('-----------')
    print ('   |  |')
    print (' ' + board[1] + ' | ' + board[2] + '| ' + board[3])
    print ('   |  |')

test_board = ['0', '1', '2', '3', '4', '5','6','7','8', '9']
display_board(test_board)

# take in player input and assign their marker as X or O
def player_input():
    pass

# takes board list object, a marker (X or O) and a position (1-9) and assigns to the board
def place_marker(board, marker, position):
    pass

# takes in a board and a mark (X or O) and checks to see if that mark has won
def win_check(board, mark):
    pass

# randomly decide who goes first
def choose_first():
    pass

# returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):
    pass

# checks if board is full and returns boolean. True if full, otherwise False
def full_board_check(board):
    pass

# asks for player's next position (1-9) and then uses space_check if it's free.
# if it's a free position, return the position for later use
def player_choice(board):
    pass

# does player want to play again? returns boolean
def replay():
    pass
    


