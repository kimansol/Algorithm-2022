# https://www.acmicpc.net/problem/23289
# 백준23289 / 온풍기 안녕(삼성 기출) / 구현,시뮬레이션
# 2022.02.10
import copy
from collections import deque

def heat(hd,hx,hy):
    q = deque()
    q.append((hd,hx+dir[hd][0],hy+dir[hd][1],5))
    flag = [[0]* C for _ in range(R)]
    while q:
        d,x,y,n = q.popleft()
        board[x][y] += n
        if n>1:
            if 0 <= x + dir[d][0] < R and 0 <= y + dir[d][1] < C:
                if [x,y,d] not in wall and flag[x+dir[d][0]][y+dir[d][1]] == 0:
                    q.append((d,x+dir[d][0],y+dir[d][1],n-1))
                    flag[x + dir[d][0]][y + dir[d][1]] = 1
            if 0 <= x + dir[(d + 4 - 1) % 4][0] + dir[d][0] < R and 0 <= y + dir[(d + 4 - 1) % 4][1] + dir[d][1] < C:
                if [x+dir[(d+4-1)%4][0],y+dir[(d+4-1)%4][1],d] not in wall and [x,y,(d+4-1)%4] not in wall:
                    if flag[x+dir[(d+4-1)%4][0]+dir[d][0]][y+dir[(d+4-1)%4][1]+dir[d][1]] == 0:
                        q.append((d,x+dir[(d+4-1)%4][0]+dir[d][0],y+dir[(d+4-1)%4][1]+dir[d][1], n-1))
                        flag[x + dir[(d + 4 - 1) % 4][0] + dir[d][0]][y + dir[(d + 4 - 1) % 4][1] + dir[d][1]] = 1
            if 0 <= x + dir[(d + 1) % 4][0] + dir[d][0] < R and 0 <= y + dir[(d + 1) % 4][1] + dir[d][1] < C:
                if [x+dir[(d+1)%4][0],y+dir[(d+1)%4][1],d] not in wall and [x,y,(d+1)%4] not in wall:
                    if flag[x+dir[(d+1)%4][0]+dir[d][0]][y+dir[(d+1)%4][1]+dir[d][1]] == 0:
                        q.append((d,x+dir[(d+1)%4][0]+dir[d][0],y+dir[(d+1)%4][1]+dir[d][1], n-1))
                        flag[x+dir[(d+1)%4][0]+dir[d][0]][y+dir[(d+1)%4][1]+dir[d][1]] = 1

def spread():
    tmp = copy.deepcopy(board)
    for i in range(R):
        for j in range(C):
            for d in range(4):
                if [i, j, d] in wall:
                    continue
                nx, ny = i + dir[d][0], j + dir[d][1]
                if 0 <= nx < R and 0 <= ny < C:
                    if tmp[nx][ny] > tmp[i][j]:
                        board[i][j] += (tmp[nx][ny] - tmp[i][j]) // 4
                    else:
                        board[i][j] -= (tmp[i][j] - tmp[nx][ny]) // 4

def sidedown():
    x, y = 0,1
    d = 3
    while 1:
        if board[x][y] >= 1:
            board[x][y] -= 1
        if x == 0 and y == 0:
            break
        nx,ny = x+ dir[d][0], y+ dir[d][1]
        if nx <0 or ny< 0 or nx >= R or ny >= C:
            d= (d+1)%4
            nx,ny = x+ dir[d][0], y+ dir[d][1]
        x,y = nx, ny

def check():
    for x, y in temp:
        if board[x][y] < K:
            return 0
    return 1


R, C, K = map(int,input().split(' '))
board = [list(map(int,input().split(' '))) for _ in range(R)]
W = int(input())
walllist = [list(map(int,input().split(' '))) for _ in range(W)]

ans = 0
heater = []
temp = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 5:
            temp.append([i,j])
            board[i][j] = 0
        elif board[i][j] > 0:
            if board[i][j] == 1:
                heater.append([3, i, j])
            elif board[i][j] == 4:
                heater.append([0, i, j])
            else:
                heater.append([board[i][j]-1,i,j])
            board[i][j] = 0
wall = []
for x,y,t in walllist:
    if t == 0:
        wall.append([x-1,y-1,2])
        wall.append(([x-2,y-1,0]))
    if t == 1:
        wall.append([x-1,y-1,3])
        wall.append([x-1,y,1])

dir = [[1,0],[0,-1],[-1,0],[0,1]]

while ans < 101:
    for hd,hx,hy in heater:
        heat(hd,hx,hy)
    spread()
    sidedown()
    ans += 1
    if check():
        break

print(ans)



