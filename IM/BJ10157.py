# https://www.acmicpc.net/problem/10157
# 백준 10157/ 자리배정 / 실버4
# 2022.01.20


def find():
    if K > N*M:
        print(0)
        return
    board = [[0] * M for _ in range(N)]
    x,y = N-1,0
    dir = [[-1,0],[0,1],[1,0],[0,-1]]#북동남서
    d = 0
    for i in range(1,N*M+1):
        board[x][y] = i
        if i == K:
            print(f"{y+1} {N-x}")
            break
        nx, ny = x + dir[d][0], y+ dir[d][1]
        if nx<0 or ny <0 or nx >=N or ny>=M or board[nx][ny] != 0:
            d = (d+1)%4
            nx, ny = x + dir[d][0], y + dir[d][1]
        x, y = nx, ny


M, N = map(int, input(). split())
K = int(input())
find()