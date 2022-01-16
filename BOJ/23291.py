##백준23289 / 온풍기 안녕(삼성 기출) / 구현,시뮬레이션
## 2022.01.15

from collections import deque

R, C, K = map(int,input().split(' '))
board = [list(map(int,input().split(' '))) for _ in range(R)]
W = int(input())
walllist = [list(map(int,input().split(' '))) for _ in range(W)]
ans = 0
heater = []
sample = []
wall = []
dir = [[0,-1] , [-1,0] , [0,1] , [1,0]] #좌상우하

for i in range(R):
    for j in range(C):
        if board[i][j] == 5:
            board[i][j] = 0
            sample.append([i,j])
        if board[i][j] in [1,2,3,4]:
            dd = 0
            if board[i][j] == 1:
                dd = 2
            elif board[i][j] == 2:
                dd = 0
            elif board[i][j] == 3:
                dd = 1
            else:
                dd = 3
            heater.append([i,j,dd])
            board[i][j] = 0

for ww in walllist:
    if ww[2] == 0:
        wall.append([ww[0]-1,ww[1]-1,1])
        wall.append([ww[0]-2,ww[1]-1,3])
    if ww[2] == 1:
        wall.append([ww[0]-1,ww[1]-1,2])
        wall.append([ww[0]-1,ww[1],0])


def heat():
    hque = deque()
    for x,y,d in heater:
        hque.append((x + dir[d][0] , y + dir[d][1] , d , 5))
        flag = [[0 for _ in range(C)] for _ in range(R)]
        while hque:
            x,y,d,p = hque.popleft()
            board[x][y] += p
            if p > 1:
                if [x,y,d-1] not in wall and [x + dir[d-1][0],y + dir[d-1][1],d] not in wall:
                    nx, ny = x + dir[d-1][0] + dir[d][0], y + dir[d-1][1] + dir[d][1]
                    if nx >= 0 and ny >= 0 and nx < R and ny < C and flag[nx][ny] == 0:
                        hque.append((nx, ny , d, p-1))
                        flag[nx][ny] = 1
                if [x, y, d] not in wall:
                    nx, ny = x + dir[d][0], y + dir[d][1]
                    if nx >= 0 and ny >= 0 and nx < R and ny < C and flag[nx][ny] == 0:
                        hque.append((nx, ny , d, p-1))
                        flag[nx][ny] = 1

                if [x, y, d + 1] not in wall and [x + dir[(d + 1)%4][0], y + dir[(d + 1)%4][1], d] not in wall:
                    nx, ny = x + dir[(d + 1)%4][0] + dir[d][0], y + dir[(d + 1)%4][1] + dir[d][1]
                    if nx >= 0 and ny >= 0 and nx < R and ny < C and flag[nx][ny] == 0:
                        hque.append((nx, ny, d, p - 1))
                        flag[nx][ny] = 1



def spread():
    updown = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            for k in range(4):
                nx,ny = i + dir[k][0], j + dir[k][1]
                if [i, j, k] in wall:
                    continue
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                if board[i][j] - board[nx][ny] >= 4:
                    updown[i][j] -= (board[i][j] - board[nx][ny]) // 4
                    updown[nx][ny] += (board[i][j] - board[nx][ny]) // 4


    for i in range(R):
        for j in range(C):
            board[i][j] += updown[i][j]

def sidedown():
    for i in range(C):
        if board[0][i] != 0:
            board[0][i] -= 1
        if board[R-1][i] != 0:
            board[R-1][i] -= 1
    for j in range(1,R-1):
        if board[j][0] != 0:
            board[j][0] -= 1
        if board[j][C-1] != 0:
            board[j][C-1] -= 1

def check(): ##모든 sample위치의 온도가 K이상인지
    cnt = 0
    allpass = len(sample)
    for x,y in sample:
        if board[x][y] >= K:
            cnt += 1
    return 1 if cnt < allpass else 0


flag = 1
while flag:
    heat()
    spread()
    sidedown()
    ans += 1
    flag = check()
    if ans > 100:
        flag = 0

print(ans)