

chess_board = []

def checking_quarters(queen_pos):
    global chess_board
    step = queen_pos[1]
    if queen_pos[0] != 0 and queen_pos[1] != (len(chess_board)-1):
        for i in range(queen_pos[0]-1, 0, -1):
            step +=1
            if chess_board[i][step] == 1:
                return  False
            if step == len(chess_board)-1:
                break
    step = queen_pos[1]
    if queen_pos[0] != (len(chess_board)-1) and queen_pos[1] != (len(chess_board)-1):
        for i in range(queen_pos[0]+1, len(chess_board), 1):
            step += 1
            if chess_board[i][step] == 1:
                return False
            if step == len(chess_board)-1:
                break
    step = queen_pos[1]
    if queen_pos[0] != 0 and queen_pos[1] != 0:
        for i in range(queen_pos[0]-1, 0, -1):
            step -= 1
            if chess_board[i][step] == 1:
                return False
            if step == 0:
                break
    step = queen_pos[1]
    if queen_pos[0] != (len(chess_board) -1) and queen_pos[1] != 0:
        for i in range(queen_pos[0] + 1, len(chess_board), 1):
            step -= 1
            if chess_board[i][step] == 1:
                return False
            if step == 0:
                break
    return True


def check_position(pos_queens):
    global chess_board
    if sum(chess_board[pos_queens[0]]) >= 1:
        return False
    for i in range(len(chess_board)):
        if chess_board[i][pos_queens[1]] == 1:
            return False
    return checking_quarters(pos_queens)


def creating_chessboard(len_board: int, list_placement: list):
    # матрица доски
    global chess_board
    chess_board = list_ = [[0 for _ in range(len_board)] for _ in range(len_board)]
    for elem in list_placement:
        i, j = elem
        chess_board[i-1][j-1] = 1


def checking_placement_queens(list_placement: list) -> bool:
    global chess_board
    for elem in list_placement:
        i, j = elem
        chess_board[i - 1][j - 1] = 0
        if check_position((i-1, j-1)) is False:
            return False
        else:
            chess_board[i - 1][j - 1] = 1
    return True

def start_pr(len_board: int, list_placement: list) -> bool:
    creating_chessboard(len_board, list_placement)
    return checking_placement_queens(list_placement)

