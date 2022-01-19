# https://www.acmicpc.net/problem/23288
# 백준 23288/ 주사위 굴리기2 / 구현/BFS/시뮬레이션
# 2022.01.17

from collections import deque

def moveDice(cx, cy, d,dice):
    nx, ny = cx + dir[d][0], cy + dir[d][1]
    if nx <0 or ny <0 or nx>= N or ny >=M:
        d = (d+2) %4
        nx, ny = cx + dir[d][0], cy + dir[d][1]
    cx, cy = nx, ny
    if d == 0: #동
        dice[1],dice[3],dice[4],dice[5] = dice[4],dice[5], dice[3], dice[1]
    elif d == 1: #남
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif d == 2: #서
        dice[1],dice[3],dice[4],dice[5] = dice[5], dice[4], dice[1], dice[3]
    else: #북
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]

    if dice[3] > board[cx][cy]:
        d = (d+1) %4
    elif dice[3] < board[cx][cy]:
        d = d - 1 if d >= 1 else 3
    else: d = d

    return cx, cy, d, dice


def bfs(x,y):
    global ans
    flag = [[0] * M for _ in range(N)]
    que.append((x,y))
    flag[x][y] = 1
    n = board[x][y]
    while que:
        x,y = que.popleft()
        ans += n
        for i in range(4):
            nx,ny = x +dir[i][0], y+dir[i][1]
            if nx<0 or ny<0 or nx>=N or ny>=M or flag[nx][ny] == 1:
                continue
            if board[nx][ny] == n:
                que.append((nx,ny))
                flag[nx][ny] = 1


N, M, K = map(int,input().split(' ')) ##맵 세로크기, 가로 크기, 이동 하는 횟수
board = [list(map(int, input().split(' '))) for i in range(N)]
ans = 0
dice = [2,1,5,6,4,3] ## [0] back, [1] top, [2]front [3] bottom, [4] left, [5] right
dir = [[0,1],[1,0],[0,-1],[-1,0]] ## 우,하,좌,상
d = 0 #현재 방향
cx,cy = 0,0  #현재 위치
que = deque()


for i in range(K):
    cx, cy, d, dice = moveDice(cx, cy, d, dice)
    bfs(cx, cy)
print(ans)