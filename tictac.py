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
    letter = raw_input('Player 1 choose to be either X or O: ')
    if letter == 'X':
        return ['X', 'O']
    else: 
        return ['O', 'X']
    pass

# takes board list object, a marker (X or O) and a position (1-9) and assigns to the board
def place_marker(board, marker, position):
    pass

# takes in a board and a mark (X or O) and checks to see if that mark has won
def win_check(board, mark):
    return ((board[7] == board[8] == board[9]) or #across top
    (board[4] == board[5] == board[6]) or #across center
    (board[1] == board[2] == board[3]) or #across bottom
    (board[7] == board[4] == board[1]) or #down left side
    (board[8] == board[5] == board[1]) or #down center
    (board[9] == board[6] == board[3]) or #down right side
    (board[7] == board[5] == board[3]) or #diag
    (board[9] == board[5] == board[1])) or #other diag

    pass

# randomly decide who goes first
def choose_first():
    if random.randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'
    pass
# returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):
    return board[position] == ' '
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
    answer = input("Do you want to play again? Type yes or no")
    if answer == 'yes':
        return True
    else:
        return False
    pass

print('Welcome to Tic Tac Toe')

while True:
    game_on = True
    while game_on:
        # display_board(board)
        player1, player2 = player_input()
        #player 1 turn

        #player 2 turn
            #pass

    if not replay():
        break 
 


