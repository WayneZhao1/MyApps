'''
Author: Wayne Zhao
This is a Tic Toc game. Requirements:
   . 2 players should be able to play the game (both sitting at the same computer)
   . The board should be printed out every time a player makes a move
   . You should be able to accept input of the player position and then place a symbol on the board
'''
#initialize the board
board=[' ']*10
board[0]=''
#current player: 0 or 1
player=['', '']
# total steps before game ends
steps = 0

# print board
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    
# Check if there is a winner
def winner(board):
    if board[7] == board[8] == board[9] != ' ' or board[4] == board[5] == board[6] != ' ' or board[1] == board[2] == board[3]  != ' ' or \
       board[1] == board[4] == board[7] != ' ' or board[2] == board[5] == board[8] != ' ' or board[3] == board[6] == board[9] != ' ' or \
       board[1] == board[5] == board[9] != ' ' or board[7] == board[5] == board[3] != ' ' :
        return True
    else:
        return False

# Check if it is a tie   
def is_tie(board):
    for char in board:
        if char == ' ':
            return False  
    return True

# Start the game
def game_on(board, player, steps):
    # the first player picks letter 'X' or 'O'
    while True:
        mychar = input("Please pick 'X' or 'O' to start: ")
        mychar=mychar.upper()
        if mychar not in ['X', 'O']:
            print("It has to be 'X' or 'O'. Please pick again!")
        else:
            print(f"Great, you picked {mychar}. Let's start!")
            if mychar == 'X':
                player=['X','O']
            else:
                player=['O','X']
                
            break
    
    # Start the game until a player wins
    while True:
        try: 
            position=int(input(f"Player {steps%2+1} with '{player[steps%2]}', please choose a position [1-9]: "))
            if position < 1 or position > 9:
                print("Please choose a number between 1 and 9!")
                continue
            else:
                if board[position] in ['X', 'O']:
                    print("Spot already taken!")
                    continue
                else: 
                    board[position]=player[steps%2]
                    display_board(board)
                    if winner(board):
                        print(f"Player {steps%2 + 1} with '{player[steps%2]}' wins!!!")
                        break
                    elif is_tie(board):
                        print("Game over. It is a tie!")
                        break
                    else:
                        steps +=1
                        continue
        except:
            print("Please choose a number between 1 and 9!")


game_on(board, player, steps)