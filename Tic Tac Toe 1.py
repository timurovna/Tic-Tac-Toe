
def print_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    marker = ' '
    player1 = ' '
    player2 = ' '
    while marker != 'X' and marker != 'O':
        marker = input('Player1, choose X or O: ')
        player1 = marker
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'

    return player1, player2


def check_result(board):
    i = 1
    while i < 8:
        if board[i] == board[i+1] == board[i+2] and board[i] != " ":
            return board[i]
        i = i + 3
    i = 1
    while i < 4:
        if board[i] == board[i+3] == board[i+6] and board[i] != " ":
            return board[i]
        i = i + 1

    if (board[1] == board[5] == board[9] or board[3] == board[5] == board[7]) and board[5] != " ":
        return board[5]

    for i in range(1, 10):
        if board[i] == " ":
            return ""

    return "D"


def play_game_party():
    board = [' '] * 10
    (player1, player2) = player_input()
    cnt = 0
    print(player1, player2)

    while check_result(board) == "":
        player = "Player 1:"
        if cnt % 2 == 1:
            player = "Player 2:"

        players_move = ""
        while players_move.isnumeric() == False or int(players_move) not in range(0, 10) or board[int(players_move)] != " ":
            players_move = input("Please, enter your move, " + player)
        players_move = int(players_move)
        cnt += 1
        if cnt % 2 == 1:
            board[players_move] = player1
        else:
            board[players_move] = player2

        print_board(board)

        print(check_result(board))

    if check_result(board) == 'X':
        if player1 == 'X':
            print("Player 1 won")
        else:
            print("Player 2 won")
    if check_result(board) == 'O':
        if player1 == 'O':
            print("Player 1 won")
        else:
            print("Player 2 won")
    if check_result(board) == "D":
        print("Draw")


while True:
    play_game_party()
    new_game = input("Do you want to start again?: ")
    if new_game == "no":
        break
