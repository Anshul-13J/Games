from IPython.display import clear_output

def display_board(board):
    #board=[0,1,2,3,4,5,6,7,8]
    print(f' ___________\n| {board[7]} | {board[8]} | {board[9]} |\n|---.---.---|\n| {board[4]} | {board[5]} | {board[6]} |\n|---.---.---|\n| {board[1]} | {board[2]} | {board[3]} |\n ___________') 
def player_input():
    choice='wrong'
    while choice not in ['X','O','x','o']:
        choice= input('Player 1, input your choice (X or O): ')
        if choice not in ['X','O','x','o']:
            clear_output()
            print('Wrong choice, choose in "X" and "O" !')
    return choice.upper()    
def place_marker(board, marker, position):
    board[position]=marker
    display_board(board)
def win_check(board, mark):
    for i in [1,4,7]:
        if [board[i],board[i+1],board[i+2]]==[mark,mark,mark]:
     #       print('Horizontal')
            return True
    #        break
    for i in [1,2,3]:
        if [board[i],board[i+3],board[i+6]]==[mark,mark,mark]:
     #       print('Vertical' )
            return True
   #         break
 #   print([board[1],board[5],board[9]])
 #   print([board[3],board[5],board[7]])
    if [board[1],board[5],board[9]] == [mark,mark,mark]:
    #    print('Diagonal-/')
        return True
    elif [board[3],board[5],board[7]] == [mark,mark,mark]:
    #    print('Diagonal-\\')
        return True
    else: 
        return False
        
            
        
import random
def choose_first():
    x=str(random.randint(1,2))
    return 'Player'+x
def space_check(board, position):
    return board[position]==' '
def full_board_check(board):
    for i in range(1,10):
        if board[i]==' ':
            return False
    print('No Winner, better luck next time')
    return True
def player_choice(board):
    choice='wrong'
    while True:
        choice=int(input('Input your next move (1-9): '))
        clear_output()
        if  choice in range(1,10)  and space_check(board, choice):
            return choice
        else:
            print('Wrong/Invalid input')
            display_board(board)
        
def replay():
   # play_again= True
    x= input('Do you want to play Y/N: ')
    if x=='Y' or x=='y':
        return True
    elif x=='N' or x=='n':
        return False
print('WELCOME TO TIC-TAC-TOE GAME\n\nYour board looks like this, ensure your inputs accordingly! ')
example_board=[0,1,2,3,4,5,6,7,8,9]
display_board(example_board)
print('\nINSTRUCTIONS:')
print("1. Player 1 gets to choose whether he wants 'X' or 'O', other one goes to player 2")
print("2. System will choose which player will start first")
print("3. Player to complete any row, column or diagonal first will win")
print("4. You can choose to play again after the game is over")
print('\nEnjoy the GAME')
print('\n-------------------------------------------------------------'*2 )
check=True
while check:
    board= list(' '*10)
    mark1= player_input()
    if mark1 == 'X':
        mark2='O'
    else:
        mark2='X'
    starter= choose_first()
    
    if starter[-1]=='1':
        
        print(starter +' goes first!')
        while not full_board_check(board):
            display_board(board)
            print('player ' + mark1 + ' turn!')
            choice=player_choice(board)
            place_marker(board,mark1,choice)
            if win_check(board,mark1):
                print('Player '+mark1 +' wins!')
                break
            
            q=mark1
            mark1=mark2
            mark2=q
            clear_output()
    else:
        print(starter +' goes first!')
        while not full_board_check(board):
            display_board(board)
            print('player ' + mark2 + ' turn!')
            choice=player_choice(board)
            place_marker(board,mark2,choice)
            
            if win_check(board,mark2):
                print('Player '+mark2 +' wins!')
                
                break
            q=mark2
            mark2=mark1
            mark1=q
            clear_output()
    check= replay()

print('Exiting game,THANKS FOR PLAYING')

        
        
