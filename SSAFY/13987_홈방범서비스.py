from A.B import *
S(8, 'azder', 'sample_')
from collections import deque

def locate(k,i,j):
    ret = 0
    visited = [[0] *n for _ in range(n)]
    q=deque([[i,j,1]])
    visited[i][j] = 1
    while q:
        x,y,d = q.popleft()
        if board[x][y] == 1:
            ret += 1
        for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
            nx,ny = x +dx,y+dy
            if nx <0 or ny <0 or nx >= n or ny >=n:
                continue
            if visited[nx][ny] == 1:
                continue
            if d == k:
                continue
            q.append([nx,ny,d+1])
            visited[nx][ny] = 1
    return ret

def check():
    ret = 0
    for k in range(max_dis-1,-1,-1):
        pay = k*k+(k-1)*(k-1)
        for i in range(n):
            for j in range(n):
                housenum = locate(k,i,j)
                if housenum * m >= pay:
                    ret = max(housenum, ret)
        if ret:
            return ret

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_pay = sum(sum(i) for i in board) * m
    max_dis = 1
    while max_dis*max_dis+(max_dis-1)*(max_dis-1) < max_pay:
        max_dis += 1

    ans = check()
    print(f'#{test_case} {ans}')

E(8, 'azder', 'sample_')