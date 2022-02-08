# https://www.acmicpc.net/problem/20058
# 마법사 상어와 파이어스톰/ 골드4/ 20058
# 2022.02.08

import sys
from copy import deepcopy
sys.setrecursionlimit(100000)
n, q = map(int ,input().split()) ## 2*n, q번 시도
board = [list(map(int, input().split())) for _ in range(2**n)]
magics = list(map(int, input().split()))

def rota(magic):
    new_board = [[0] * 2**n for _ in range(2**n)]
    for i in range(0,2**n,2**magic):
        for j in range(0,2**n,2**magic):
            for k in range(2**magic):
                for l in range(2**magic):
                    new_board[i+k][j+l] = board[i+2**magic-1-l][j+k]
    return new_board

def melt():
    new_board = deepcopy(board)
    for i in range(2**n):
        for j in range(2**n):
            cnt = 0
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx, ny = i + dx, j + dy
                if nx < 0 or ny < 0 or nx >= 2**n or ny >= 2**n:
                    continue
                if new_board[nx][ny] != 0:
                    cnt += 1
            if cnt < 3 and new_board[i][j] > 0:
                board[i][j] -= 1

def dfs(x,y):
    board[x][y] = 0
    ret = 1
    for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
        nx,ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>=2**n or ny>=2**n or board[nx][ny] == 0:
            continue
        ret += dfs(nx,ny)

    return ret

for magic in magics:
    board = rota(magic)
    melt()

ans = 0
for line in board:
    ans += sum(line)
print(ans)

max_val=0
for i in range(2**n):
    for j in range(2**n):
        if board[i][j] > 0:
            max_val = max(max_val, dfs(i,j))
print(max_val)
