# https://programmers.co.kr/learn/courses/30/lessons/92343
# 2022카카오/레벨3/사라지는 발판
# 2022.02.14
from copy import deepcopy

def play(board,aloc,bloc,turn,cnt):
    global answer
    if turn == 0:
        x, y = aloc
    else:
        x, y = bloc

    if board[x][y] == 0:
        answer = max(answer, cnt)
        return

    dir_check = 0
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]):
            continue
        if board[nx][ny] == 0:
            continue
        if turn == 0:
            board[x][y] = 0
            new_board = deepcopy(board)
            play(new_board,[nx,ny],bloc,(turn+1)%2,cnt +1)
            board[x][y] = 1
        else:
            board[x][y] = 0
            new_board = deepcopy(board)
            play(new_board,aloc,[nx,ny],(turn+1)%2,cnt +1)
            board[x][y] = 1
        dir_check += 1
    if dir_check == 0:
        answer = max(answer, cnt)
        return

def solution(board, aloc, bloc):
    global answer
    answer = -1

    play(board,aloc,bloc,0,0)
    return answer



print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],[1, 0], [1, 2]))