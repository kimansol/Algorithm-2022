#https://www.acmicpc.net/problem/20056
# 마법사 상어와 파이어볼/골드4
# 2022.02.18

from collections import deque

n,m,k = map(int ,input().split())
fireball = [list(map(int, input().split())) for _ in range(m)]
q=deque(fireball)
##r,c,m,s,d,   위치r,c 질량 방향 속력

dir = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
board = [[[] for _ in range(n+1)] for _ in range(n+1)]

def move():
    for _ in range(len(q)):
        r,c,m,s,d = q.popleft()
        board[r][c] = []
        nx,ny = 0,0
        for _ in range(s):
            nx,ny = r + dir[d][0], c + dir[d][1]
            if nx == 0:
                nx = n
            if ny == 0:
                ny = n
            if nx >= n+1:
                nx = 1
            if ny >= n+1:
                ny = 1
            r,c= nx,ny
        q.append([nx,ny,m,s,d])

def marking():
    for _ in range(len(q)):
        r,c,m,s,d = q.popleft()
        board[r][c].append([m,s,d])

def div():
    for i in range(1,n+1):
        for j in range(1,n+1):
            fire_cnt=len(board[i][j])
            if fire_cnt > 1:
                mount_sum = 0
                speed_sum = 0
                dir_sum = 0
                for k in range(fire_cnt):
                    mount_sum += board[i][j][k][0]
                    speed_sum += board[i][j][k][1]
                    dir_sum += board[i][j][k][2] % 2
                if dir_sum == 0 or dir_sum == fire_cnt:
                    nd = 0
                else:
                    nd = 1
                if mount_sum//5 > 0:
                    for _ in range(4):
                        q.append([i,j,mount_sum//5,speed_sum//fire_cnt,nd])
                        nd += 2
                else:
                    board[i][j] = []
            elif fire_cnt == 1:
                q.append([i,j,board[i][j][0][0],board[i][j][0][1],board[i][j][0][2]])


for _ in range(k):

    move()
    marking()
    div()


ans = 0
while q:
    x,y,m,s,d = q.popleft()
    ans += m
print(ans)





