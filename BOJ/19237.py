# https://www.acmicpc.net/problem/19237
# 백준 19237 // 어른 상어(삼성 기출) // 구현, 시뮬레이션
# 2022-01-16

def shit():
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 0:
                smell[i][j] = [board[i][j], K, -1]

def moveshark(x,y,n): #[x,y,번호]
    global leave
    dirlist = movelike[n][direction[n]]
    for d in dirlist:
        nx,ny = x + dir[d][0], y +dir[d][1]
        if nx <0 or ny <0 or nx >= N or ny >= N:
            continue
        if smell[nx][ny][1] == 0:
            direction[n] = d
            board[x][y] = -1
            if smell[nx][ny][2] == -1:
                smell[nx][ny][2] = n
            elif smell[nx][ny][2] > n:
                smell[nx][ny][2] = n
                leave += 1
            elif smell[nx][ny][2] < n:
                leave += 1
            return
    for d in dirlist:
        nx, ny = x + dir[d][0], y + dir[d][1]
        if nx <0 or ny <0 or nx >= N or ny >= N:
            continue
        if smell[nx][ny][0] == n and smell[nx][ny][1] > 0:
            direction[n] = d
            board[x][y] = -1
            if smell[nx][ny][2] == -1:
                smell[nx][ny][2] = n
            return
    board[x][y] = -1
    smell[x][y][2] = n

def findshark():
     for i in range(N):
        for j in range(N):
            if board[i][j] >= 0:
                moveshark(i,j,board[i][j])

#냄새가 약해짐
def weak():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if smell[i][j][2] >= 0:
                board[i][j] = smell[i][j][2]
                smell[i][j][2] = -1


N, M, K = map(int, input().split(' '))
board = [list(map(int, input().split(' '))) for i in range(N)]
direction = list(map(int, input().split(' ')))
movelike = [[list(map(int, input().split(' '))) for i in range(4)] for i in range(M)]
smell = [[[-1,0,-1] for i in range(N)] for i in range(N)]
dir = [[-1,0],[1,0],[0,-1],[0,1]]

for i in range(M):
    direction[i] -= 1

for i in range(N):
    for j in range(N):
        board[i][j] -= 1

for i in range(M):
    for j in range(4):
        for k in range(4):
            movelike[i][j][k] -= 1
leave = 1


timer = 1
while timer:
    if timer == 1001:
        print(-1)
        break
    shit()
    findshark()
    if leave == M:
        print(timer)
        break
    weak()
    timer += 1