"""
[Module] Tic-tac-toe bot utilities.
"""
from random import randint
import requests
from urllib.parse import unquote


API_URL = "http://127.0.0.1:8000"


def is_registry_open() -> bool:
    """
    Checks if registry is available via API.
    """
    try:
        url = "{}/registry".format(API_URL)
        res = requests.get(url)

        if res.text == "true":
            return True
        elif res.text == "false":
            return False

    except:
        return False


def register_user(name: str) -> str:
    """
    Registers user in API game.
    """
    url = "{}/register_player/{}".format(API_URL, name)
    res = requests.post(url)
    player_id = res.text[1]
    return player_id


def is_my_turn(player_id: str) -> bool: 
    """
    Checks if it is our turn via API.
    """
    url = "{}/turn/{}".format(API_URL, player_id)
    res = requests.get(url)
    
    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def read_board() -> list:
    """
    Gets game board via API.
    """
    url = "{}/board".format(API_URL)
    res = requests.get(url)
    board_str = res.text
    board = [
        [board_str[1], board_str[2], board_str[3]], 
        [board_str[4], board_str[5], board_str[6]], 
        [board_str[7], board_str[8], board_str[9]]
    ]

    return board


def decide_move(board: list, player_id: str) -> [int, int]:
    """
    Decides next move to make.
    """
    r = 0
    c = 1
    if player_id == "X" and board[0][0] == "-":
        row = 0
        column = 0
        return[row, column]

    if player_id == "O" and board[1][1] == "-":
        row = 1
        column = 1
        return[row, column]

    def win1(board,r ,c):

        r = 0
        c = 1

        while r < 2:
            for i in range(len(board)):
                if c >= 3:
                    c = 1
                    
                if player_id == board[r][i] == board[c][i]:
                    if r == 0:
                        if i == 0 and board[2][0] == "-":
                            row = 2
                            column = 0
                            r = 2
                            return [row, column]
                        if i == 1 and board[2][1] == "-":
                            row = 2
                            column = 1
                            r = 2
                            return [row, column]
                        if i == 2 and board[2][2] == "-":
                            row = 2
                            column = 2
                            r = 2
                            return [row, column]
                
                    if r == 1:
                        if i == 0 and board[0][0] == "-":
                            row = 0
                            column = 0
                            r = 2
                            return [row, column]
                        if i == 1 and board[0][1] == "-":
                            row = 0
                            column = 1
                            r = 2
                            return [row, column]
                        if i == 2 and board[0][2] == "-":
                            row = 0
                            column = 2
                            r = 2
                            return [row, column]

                if player_id == board[i][r] == board[i][c]:
                    if r == 0:
                        if i == 0 and board[0][2] == "-":
                            row = 0
                            column = 2
                            r = 2
                            return [row, column]
                        if i == 1 and board[1][2] == "-":
                            row = 1
                            column = 2
                            r = 2
                            return [row, column]
                        if i == 2 and board[2][2] == "-":
                            row = 2
                            column = 2
                            r = 2
                            return [row, column]

                    if r == 1:
                        if i == 0 and board[2][0] == "-":
                            row = 0
                            column = 0
                            r = 2
                            return [row, column]
                        if i == 1 and board[1][0] == "-":
                            row = 1
                            column = 0
                            r = 2
                            return [row, column]
                        if i == 2 and board[2][0] == "-":
                            row = 2
                            column = 0
                            r = 2
                            return [row, column]

                if player_id == board[0][i] == board[2][i]:
                    if i == 0 and board[1][0] == "-":
                        row = 1
                        column = 0
                        r = 2
                        return [row, column]
                    if i == 1 and board[1][1] == "-":
                        row = 1
                        column = 1
                        r = 2
                        return [row, column]
                    if i == 2 and board[1][2] == "-":
                        row = 1
                        column = 2
                        r = 2
                        return [row, column]

                if player_id == board[i][0] == board[i][2]:
                    if i == 0 and board[0][1] == "-":
                        row = 0
                        column = 1
                        r = 2
                        return [row, column]
                    if i == 1 and board[1][1] == "-":
                        row = 1
                        column = 1
                        r = 2
                        return [row, column]
                    if i == 2 and board[2][1] == "-":
                        row = 2
                        column = 1
                        r = 2
                        return [row, column]


                if player_id == board[0][0] == board[2][2] and board[1][1] == "-" or player_id == board[0][2] == board[2][0] and board[1][1] == "-":
                    row = 1
                    column = 1
                    r = 2
                    return [row, column]

                if player_id == board[0][0] == board[1][1] and board[2][2] == "-":
                    row = 2
                    column = 2
                    r = 2
                    return [row, column]

                if player_id == board[0][2] == board[1][1] and board[2][0] == "-":
                    row = 2
                    column = 0
                    r = 2
                    return [row, column]

                if player_id == board[2][0] == board[1][1] and board[0][2] == "-":
                    row = 0
                    column = 2
                    r = 2
                    return [row, column]

                if player_id == board[2][2] == board[1][1] and board[0][0] == "-":
                    row = 0
                    column = 0
                    r = 2
                    return [row, column]

  
            r += 1
            c += 1


        return False

    def win(board,r ,c):

        r = 0
        c = 1
        
        while r < 2:
            for i in range(len(board)):

                if c >= 3:
                    c = 1
                    
                if "X" == board[r][i] == board[c][i] or "O" == board[r][i] == board[c][i]:
                    if r == 0:
                        if i == 0 and board[2][0] == "-":
                            row = 2
                            column = 0
                            r = 2
                            return [row, column]
                        if i == 1 and board[2][1] == "-":
                            row = 2
                            column = 1
                            r = 2
                            return [row, column]
                        if i == 2 and board[2][2] == "-":
                            row = 2
                            column = 2
                            r = 2
                            return [row, column]

                    if r == 1:
                        if i == 0 and board[0][0] == "-":
                            row = 0
                            column = 0
                            r = 2
                            return [row, column]
                        if i == 1 and board[0][1] == "-":
                            row = 0
                            column = 1
                            r = 2
                            return [row, column]
                        if i == 2 and board[0][2] == "-":
                            row = 0
                            column = 2
                            r = 2
                            return [row, column]

                if "X" == board[i][r] == board[i][c] or "O" == board[i][r] == board[i][c]:
                    if r == 0:
                        if i == 0 and board[0][2] == "-":
                            row = 0
                            column = 2
                            r = 2
                            return [row, column]
                        if i == 1 and board[1][2] == "-":
                            row = 1
                            column = 2
                            r = 2
                            return [row, column]
                        if i == 2 and board[2][2] == "-":
                            row = 2
                            column = 2
                            return [row, column]

                    if r == 1:
                        if i == 0 and board[2][0] == "-":
                            row = 0
                            column = 0
                            r = 2
                            return [row, column]
                        if i == 1 and board[1][0] == "-":
                            row = 1
                            column = 0
                            r = 2
                            return [row, column]
                        if i == 2 and board[2][0] == "-":
                            row = 2
                            column = 0
                            r = 2
                            return [row, column]

                if "X" == board[0][i] == board[2][i] or "O" == board[0][i] == board[2][i]:
                    if i == 0 and board[1][0] == "-":
                        row = 1
                        column = 0
                        r = 2
                        return [row, column]
                    if i == 1 and board[1][1] == "-":
                        row = 1
                        column = 1
                        r = 2
                        return [row, column]
                    if i == 2 and board[1][2] == "-":
                        row = 1
                        column = 2
                        r = 2
                        return [row, column]

                if "X" == board[i][0] == board[i][2] or "O" == board[i][0] == board[i][2]:
                    if i == 0 and board[0][1] == "-":
                        row = 0
                        column = 1
                        r = 2
                        return [row, column]
                    if i == 1 and board[1][1] == "-":
                        row = 1
                        column = 1
                        r = 2
                        return [row, column]
                    if i == 2 and board[2][1] == "-":
                        row = 2
                        column = 1
                        r = 2
                        return [row, column]


                if "X" == board[0][0] == board[2][2] and board[1][1] == "-" or "X" == board[0][2] == board[2][0] and board[1][1] == "-" or "O" == board[0][0] == board[2][2] and board[1][1] == "-" or "O" == board[0][2] == board[2][0] and board[1][1] == "-":
                    row = 1
                    column = 1
                    r = 2
                    return [row, column]

                if "X" == board[0][0] == board[1][1] and board[2][2] == "-" or "O" == board[0][0] == board[1][1] and board[2][2] == "-":
                    row = 2
                    column = 2
                    r = 2
                    return [row, column]

                if "X" == board[0][2] == board[1][1] and board[2][0] == "-" or "O" == board[0][2] == board[1][1] and board[2][0] == "-":
                    row = 2
                    column = 0
                    r = 2
                    return [row, column]

                if "X" == board[2][0] == board[1][1] and board[0][2] == "-" or "O" == board[2][0] == board[1][1] and board[0][2] == "-":
                    row = 0
                    column = 2
                    r = 2
                    return [row, column]

                if "X" == board[2][2] == board[1][1] and board[0][0] == "-" or "O" == board[2][2] == board[1][1] and board[0][0] == "-":
                    row = 0
                    column = 0
                    r = 2
                    return [row, column]

            r += 1
            c += 1


        return False

    r = 0
    c = 1
    win1(board, r, c)

    if win1(board, r, c) == False:
        win(board, r, c)

    if win1(board, r, c) != False:
        return win1(board, r, c)

    if win(board, r, c) == False:
        if player_id == "O" and board[0][0] == board[2][2] == "X" or player_id == "O" and board[0][2] == board[2][0] == "X":
            row = 1
            column = 2
            return[row, column]

        if board[0][0] == "-":
            row = 0
            column = 0
            return[row, column]
            
        if board[0][2] == "-":
            row = 0
            column = 2
            return[row, column]

        if board[2][0] == "-":
            row = 2
            column = 0
            return[row, column]

        if board[2][2] == "-":
            row = 2
            column = 2
            return[row, column]

        else:
            row = 1
            column = 1
            return[row, column]

    else:
        return win(board, r, c)


def validate_move(board: list, move: list) -> bool:
    """
    Checks if the desired next move hits an empty position.
    """
    row, col = move[0], move[1]
    if board[row][col] == "-":
        return True

    return False


def send_move(player_id: str, move: list) -> None:
    """
    Sends move to API.
    """
    row, col = move[0], move[1]
    url = "{}/move/{}/{}/{}".format(API_URL, player_id, row, col)
    res = requests.post(url)
    return None


def does_game_continue() -> bool:
    """
    Checks if the current match continues via API.
    """
    url = "{}/continue".format(API_URL)
    res = requests.get(url)

    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def print_board(board: list) -> None:
    '''
    Prints the baord in console to watch the game.
    '''
    print("\nCurrent board: \n")
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("----------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("----------")
    print(board[2][0], "|", board[2][1], "|", board[2][2], "\n")
