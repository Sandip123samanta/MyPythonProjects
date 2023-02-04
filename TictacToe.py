#print the board
from IPython.display import clear_output

def display_board(board):
    clear_output()     #To clear output in the Notebook you can use the clear_output() function
    print(board[1]+' | '+board[2] +' | '+board[3])
    print("----------")
    print(board[4]+' | '+board[5]+' | '+board[6])
    print("----------")
    print(board[7]+' | '+board[8]+' | '+board[9])

#assigning 'x' or 'O' to individual players
def user_assign():
    
    assign = ''
    while not(assign == 'O' or assign == 'X'):
        assign = input("Player1: choose 'x'or'O': ").upper()
        if assign == 'X':
            return ('X','O')
        else:
            return ('O','X')

#place the mark in the particular position

def place_mark(board,mark,position):
    
    board[position] = mark

#check for win
def win_check(board,mark):
    return ((board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark) or (board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark))
        
#randomly choose player
import random

def choose_first():
    
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'

#check if space available

def space_check(board,position):
    
    return board[position] == ' '

#check if the board is full:

def check_full(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#ask for position where the player want to give their mark

def player_choice(board):
    
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose position (1-9): "))
        
    return position

#want to replay or not 

def replay():
    
    choice = input("Play again? enter (yes/no): ")
    return choice == 'yes'

#Tic Tac Toe game

print("\n\n\t\t\t\t!!!Welcome to the Tic Tac Toe!!!")
while True:
    
    
    the_board = [' ']*10
    
    Player1_marker,Player2_marker = user_assign()
    
    print(f'player1 got {Player1_marker} and player2 got {Player2_marker}')
    
    turn = choose_first()
    
    print(turn+ ' will go first')
    
    play_game = input("Ready to play the game (y/n)?").upper()
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        
        if turn == 'Player1':
            
            display_board(the_board)
            
            position = player_choice(the_board)
            
            place_mark(the_board,Player1_marker,position)
            
            if win_check(the_board,Player1_marker):
                
                display_board(the_board)
                
                print("Player1 won the game")
                
                game_on = False
            else:
                if check_full(the_board):
                    
                    display_board(the_board)
                    
                    print("It's a Tie!!!")
                    
                    game_on = False
                
                else:
                    
                    turn = 'Player2'
        else:
            display_board(the_board)
            
            position = player_choice(the_board)
            
            place_mark(the_board,Player2_marker,position)
            
            if win_check(the_board,Player2_marker):
                
                display_board(the_board)
                
                print("Player2 won the game")
                
                game_on = False
            else:
                if check_full(the_board):
                    
                    display_board(the_board)
                    
                    print("It's a Tie!!!")
                    
                    game_on = False
                
                else:
                    
                    turn = 'Player1'
    
    if not replay():
        break              #break from the while loop