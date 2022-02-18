#https://www.acmicpc.net/problem/19238
#스타트택시/골드4
#2022.02.18
from collections import deque

n,m,k = map(int, input().split()) #맵크기, 승객 수, 연료 양
board = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())
x -= 1
y -= 1
idx = 2
destination = []
for i in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    board[x1-1][y1-1] = idx
    destination.append([x2-1,y2-1])
    idx += 1

def find_sonim(x,y):
    if board[x][y] >= 2:
        tmp = board[x][y]
        board[x][y] = 0
        return x,y,0,tmp
    sonim_list = []
    q = deque()
    visit = [[-1] * n for _ in range(n)]
    q.append([x,y])
    visit[x][y] = 0
    min_dest = -1
    while q:
        x,y = q.popleft()
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx,ny = x +dx, y+ dy
            if visit[x][y] == min_dest:
                continue
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if visit[nx][ny] != -1 or board[nx][ny] == 1:
                continue
            visit[nx][ny] = visit[x][y] + 1
            if board[nx][ny] >= 2:
                sonim_list.append([nx,ny,board[nx][ny]])
                min_dest = visit[nx][ny]
            else:
                q.append([nx,ny])
    if min_dest == -1:
        return 0,0,10e999,0

    sonim_list = sorted(sonim_list, key=lambda x : (x[0],x[1]))
    x,y,sonim = sonim_list[0][0], sonim_list[0][1], sonim_list[0][2]
    board[x][y] = 0
    return x,y,min_dest,sonim

def find_dest(x,y,sonim):
    q = deque()
    visit = [[-1] * n for _ in range(n)]
    q.append([x, y])
    visit[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visit[nx][ny] != -1 or board[nx][ny] == 1:
                continue
            visit[nx][ny] = visit[x][y] + 1
            if [nx,ny] == destination[sonim-2]:
                return nx,ny,visit[nx][ny]
            else:
                q.append([nx, ny])
    return 0,0,10e999

cnt = 0
while cnt < m:
    x,y,used_oil,sonim = find_sonim(x,y)
    k -= used_oil
    if k <= 0:
        k = -1
        break
    x,y,used_oil = find_dest(x,y,sonim)
    k -= used_oil
    if k < 0:
        k = -1
        break
    else:
        k += used_oil * 2
        cnt += 1

print(k)