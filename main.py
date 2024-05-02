# import goes here #
import random
# import ends here #
print("----Welcome to the Tic-tac-toe Game-Board----")

board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

# Displaying the board of tic-tac-toe game board 
def display_board(board):

    '''This representation provides a clear visual understanding of the board layout
          | |
         -----
          | | 
         -----
          | |  '''

    print("\t",board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("\t"  , "-----")
    print("\t",board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("\t"  , "-----")
    print("\t",board[2][0] + "|" + board[2][1] + "|" + board[2][2]) 
    return board

# rather player choose symbol "X" or "O".
def choose_symbol():
    
    while True:

        symbol = input("Choose symbol X or O: ")
        player = None
        computer = None

        if symbol == "X":
            player = "X"
            computer = "O"

        elif symbol == "O":
            player = "O"
            computer = "X"

        else:
            print("Invalid input or character, Please enter a correct symbol: ")
            continue

        return player,computer
        
def player_move(board,symbol):

    '''Player should make a move between 0 and 8 '''

    while True:

        try:
            position = int(input("Enter the position of row (0-8): "))
            print("Player's Turn")
            
            if position >= 0 and position <= 8:

                row = position // 3
                column = position % 3

                if board[row][column] == "-":
                    board[row][column] = symbol
                    break

                else:
                    print("The position is already taken.")
            else:
                print("Invalid number, Please enter a number between (0-8):")

        except ValueError:
            print("Invalid character or a string, Please enter a number")

    return board

def computer_move(board,symbol):

    '''In this function computer is making a move random against player'''

    print("Computer's Turn")

    while True:

        row = random.randint(0,2)
        column = random.randint(0,2)

        if board[row][column] == "-":
            board[row][column] = symbol
            break
        
    return board

def checkwinner(board):

    # it will check if palyer-or-computer-wins-row-wise
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "-":
            return row[0]

    # it will check if palyer-or-computer-wins-column-wise
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "-":
            return board[0][col]

    # it will check if player or computer wins diagonally
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]

    return None

# if all board is fill then the match will goes draw
def check_tie(board):       
    
    for row in board:
       for column in row:
           if column == "-":
               return False
    return True
    
display_board(board)
p_symbol, c_symbol = choose_symbol()

while True:

    display_board(board)
    player_move(board, p_symbol)

    # check if player has won
    if checkwinner(board) == p_symbol:
        display_board(board)
        print("Congrats! You win.")
        break
    
    # check if computer has won
    elif checkwinner(board) == c_symbol:
        print("Computer wins!")
        display_board(board)
        break
    
    # check if match was draw
    elif check_tie(board):
        display_board(board)
        print("It's Tie!")
        break

    display_board(board)
    computer_move(board,c_symbol)
    
    # check player has won after computer's move
    if checkwinner(board) == p_symbol:
        display_board(board)
        print("Congrats! You win.")
        break
    
    # check computer has won after computer's move
    elif checkwinner(board) == c_symbol:
        display_board(board)
        print("Computer Wins!")
        break
    
    # check for a tie after computer's move
    elif check_tie(board):
        display_board(board)
        print("It's tie")
        break 