#https://www.acmicpc.net/problem/13460
#구슬탈출2/ 골드1
# 2022.02.26
from copy import deepcopy

n,m =map(int, input().split())
board = [list(map(str, input())) for i in range(n)]

def move(board,r,c):
    for i in range(1, r-1):
        for j in range(1, c-1):
            if board[i][j] == 'O':
                for k in range(j+1, c-1):
                    if board[i][k] == 'R':
                        for l in range(k+1, c-1):
                            if board[i][l] == 'B':
                                return board, 2
                            elif board[i][l] == '#':
                                return board, 1
                        return board, 1
                    elif board[i][k] == 'B':
                        return board, 2
                    elif board[i][k] == '#':
                        break
            elif board[i][j] == '.':
                for k in range(j + 1, c - 1):
                    if board[i][k] == 'R' or board[i][k] == 'B':
                        board[i][j], board[i][k] = board[i][k], board[i][j]
                        break
                    elif board[i][k] == 'O':
                        break
                    elif board[i][k] == '#':
                        break
    return board, 0

def dfs(cnt, board, end_flag, r, c): ##이동 횟수, 현재보드, end_flag 0: 아직 모름 1:성공 2:실패
    global ans
    if end_flag == 1: #성공 했을 때
        ans = min(ans, cnt)
        return
    if cnt >= ans or end_flag == 2: #현재 이동 횟수가 최소 답 보다 클때, 이미 실패를 했을때
        return
    for i in range(4):
        moved_board, end_flag = move(deepcopy(board),r,c)
        if end_flag == 0 and moved_board == board:
            board = list(map(list, zip(*board[::-1])))
            r, c = c, r
            continue
        dfs(cnt+1, moved_board, end_flag, r,c)
        board = list(map(list, zip(*board[::-1])))
        r, c = c, r

ans = 11
dfs(0, board,0 ,n ,m)
print(-1 if ans == 11 else ans)

