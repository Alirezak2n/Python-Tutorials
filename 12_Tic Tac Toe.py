# global variables


board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_", ]

game_still_going = True

winner = None

current_player = 'X'


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | ")


def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print('Tie')


def handle_turn(player):
    print(player + "'s turn")
    position = input("choose a number from 1-9: ")

    valid = False
    while not valid:
        # baraye check kardane jaye khali
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("give another number: ")
        # baraye check kardane adad budan
        position = int(position) - 1

        if board[position] == "_":
            valid = True
        else:
            print("space is not empty")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner
    # migim global yani variable k birune funcion hast
    # ro mikhaym

    # check all methods of rows
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagnoals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    # print(row_1) khate bala yani har kodum az row ha
    # true bashan va False nabashan
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
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[3]
    elif column_3:
        return board[6]
    return


def check_diagnoals():
    global game_still_going
    diagnoal_1 = board[0] == board[4] == board[8] != "_"
    diagnoal_2 = board[6] == board[4] == board[2] != "_"

    if diagnoal_1 or diagnoal_2:
        game_still_going = False
    if diagnoal_1:
        return board[0]
    elif diagnoal_2:
        return board[6]
    return


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = "O"
    else:
        current_player = 'X'
    return


def check_if_tie():
    global game_still_going
    if '_' not in board:
        game_still_going = False
    return



play_game()

