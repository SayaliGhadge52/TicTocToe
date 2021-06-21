#TIC TAC TOE

#Algorithm:
'''-->3 * 3 board
-->handled the turns
-->players required(X and O)
-->decide which player will start the game
-->flip players (or) swap the players
-->check who is the winner:
   --->rows
   --->columns
   -->diagonals
-->declare that winner
-->display the result as draw'''

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

currentplayer = "X"

gameisgoing=True

winner=None

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def handle_turns():
    global gameisgoing
    position=int(input("Enter the position number:"))
    board[position]=currentplayer

def swap_players():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    elif currentplayer == "O":
        currentplayer = "X"

def check_who_is_winner():
    global winner
    rowwinner=check_row()
    colwinner=check_column()
    diawinner=check_dia()
    check_draw()

    if rowwinner:
        winner=rowwinner
    elif colwinner:
        winner=colwinner
    elif diawinner:
        winner=diawinner

def check_row():
    global gameisgoing
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        gameisgoing=False

    if row1:
        return board[2]
    elif row2:
        return board[5]
    elif row3:
        return board[6]

def check_column():
    global gameisgoing
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        gameisgoing=False

    if col1:
        return board[6]
    elif col2:
        return board[1]
    elif col3:
        return board[5]

def check_dia():
    global gameisgoing
    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"


    if dia1 or dia2:
        gameisgoing=False

    if dia1:
        return board[4]
    elif dia2:
        return board[6]

def check_draw():
    global gameisgoing
    if "-" not in board:
        gameisgoing = False
        print("Match is Drawn")

def play_game():
    global gameisgoing
    while gameisgoing:
        display_board()

        handle_turns()

        swap_players()

        check_who_is_winner()

    if winner=="X":
        print("X is winner")
    elif winner=="O":
        print("O is winner")


play_game()
