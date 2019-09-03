import random

board = ['-','-','-','-','-','-','-','-','-']
game_still_going = True
winner = None

current_player = random.randint(0,1)
if current_player==0:
    current_player='X'
elif current_player==1:
    current_player='O'

def display_board(board):
    print (board[0]+' | '+board[1]+' | '+board[2])
    print (board[3]+' | '+board[4]+' | '+board[5])
    print (board[6]+' | '+board[7]+' | '+board[8])

print (display_board(board))