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