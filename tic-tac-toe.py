import random

board = ['-','-','-','-','-','-','-','-','-']
game_still_going = True
winner = None

current_player = random.randint(0,1)
if current_player==0:
    current_player='X'
elif current_player==1:
    current_player='O'

def display_board():
    print (board[0]+' | '+board[1]+' | '+board[2])
    print (board[3]+' | '+board[4]+' | '+board[5])
    print (board[6]+' | '+board[7]+' | '+board[8])

def handle_turn(current_player):
    valid = True
    print (current_player+"'s turn")
    position = input("Choose position (1-9): ")
    while valid:
        while position not in '1 2 3 4 5 6 7 8 9'.split():
            position = input("Please choose from (1-9): ")
        position = int(position)-1
        if board[position]=='-':
            valid=False
        else:
            print("Occupied")
        board[position]=current_player
        display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner
    rows_winner = check_rows()
    columns_winner = check_columns()
    diagonal_winner = check_diagonals()

    if rows_winner:
        winner = rows_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going
    row_1 = board[0]==board[1]==board[2]!='-'
    row_2 = board[3]==board[4]==board[5]!='-'
    row_3 = board[6]==board[7]==board[8]!='-'
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going
    column_1 = board[0]==board[3]==board[6]!='-'
    column_2 = board[1]==board[4]==board[7]!='-'
    column_3 = board[2]==board[5]==board[8]!='-'
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    diagonal_1 = board[0]==board[4]==board[8]!='-'
    diagonal_2 = board[2]==board[4]==board[6]!='-'
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return
def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False

