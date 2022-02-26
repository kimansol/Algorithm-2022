# https://www.acmicpc.net/problem/12100
# 2048(Easy)/골드2
# 2022.02.17

from copy import deepcopy

def move(board):
    #인접한 2개 합치기
    for i in range(n):
        for j in range(n):
            for k in range(j+1,n):
                if board[i][j] != 0 and board[i][k] !=0:
                    if board[i][j] == board[i][k]:
                        board[i][j] *= 2
                        board[i][k] = 0
                        break
                    else:
                        break
    #왼쪽으로 이동
    for i in range(n):
        idx = 0
        for j in range(n):
            if board[i][j] !=0:
                board[i][j],board[i][idx] = 0,board[i][j]
                idx += 1
    return board

def play(board, cnt):
    if cnt == 5:
        global ans
        tmp = 0
        for line in board:
            tmp = max(tmp,max(line))
        ans = max(ans, tmp)
        # global a
        # a +=1
        # print(a)
        return

    for i in range(4):
        board = list(map(list, zip(*board[::-1])))
        play(move(deepcopy(board)),cnt+1)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# a = 0
play(board, 0)
print(ans)