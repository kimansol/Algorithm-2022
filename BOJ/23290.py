## 백준 23290/마법사 상어와 복제(삼성 기출)/ 구현,시뮬레이션
## 2022.01.13

from collections import deque
from itertools import product

M, S = map(int,input().split(' '))
board = [[0,0,0,0] for _ in range(4)]
smell = [[0,0,0,0] for _ in range(4)]

fish = deque()
copyfish = deque()
for i in range(M):
    x,y,d = map(int, input().split(' '))
    board[x-1][y-1] += 1
    fish.append((x-1,y-1,d-1))

sx, sy = map(int,input().split())
shark = [sx-1,sy-1]
alivefish = 0

fdir = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
sdir = [[0,1],[1,0],[0,-1],[-1,0]]

def copymove(): ## 살아있는 상어를 copyfish queue에 복사후 이동
    n = len(fish)
    for ii in range(n):
        x,y,d = fish.popleft()
        copyfish.append((x,y,d))

        for i in range(9):
            nd = d - i
            if nd < 0:
                nd = 8 + nd
            nx,ny = x + fdir[nd][0], y + fdir[nd][1]
            if i == 8:
                nx,ny,nd = x,y,d
            if nx< 0 or ny <0 or nx > 3 or ny > 3:
                continue
            if smell[nx][ny] !=0:
                continue
            if nx == shark[0] and ny == shark[1]:
                continue
            break

        board[x][y] -= 1
        board[nx][ny] += 1
        fish.append((nx,ny,nd))

def simul(movelist,x,y): ##샤크의 모든 이동경로를 이동후 먹은 물고기수 계산
    cnt = 0
    cx, cy = x, y
    copymap = [[0,0,0,0] for _ in range(4)]
    for ii in range(4):
        for jj in range(4):
            copymap[ii][jj] = board[ii][jj]
    for j in movelist:
        nx = cx + sdir[j][0]
        ny = cy + sdir[j][1]
        if nx < 0 or ny < 0 or nx > 3 or ny > 3:
            return -1
        if copymap[nx][ny] != 0:
            cnt += copymap[nx][ny]
            copymap[nx][ny] = 0
        cx, cy = nx, ny
    return cnt

def sharkmove(): ##상어의 이동경로중 가장 많은 물고기를 먹을수 있는 경로 선택 후 이동
    movelist = list(product([0,1,2,3],repeat = 3))
    eatmax = 0
    eatlist = (3,3,3)
    x,y = shark[0],shark[1]
    for i in movelist:
        cnt = simul(i,x,y)
        if cnt >= eatmax:
            eatmax = cnt
            eatlist = i
    cx, cy = x, y
    for dir in eatlist:
        nx = cx + sdir[dir][0]
        ny = cy + sdir[dir][1]
        if board[nx][ny] != 0:
            board[nx][ny] = 0
            smell[nx][ny] = 3
        cx, cy = nx, ny
    shark[0],shark[1] = cx, cy

def smelldown():
    for i in range(4):
        for j in range(4):
            if smell[i][j] != 0:
                smell[i][j] -= 1

def fishcopy(): ## 살아있는 물고기와 복사된 물고기를 정리하여 fish큐에 추가
    nn = len(fish)
    for i in range(nn):
        x,y,d = fish.popleft()
        if board[x][y] != 0:
            fish.append((x,y,d))


    n = len(copyfish)
    for i in range(n):
        x,y,d = copyfish.popleft()
        board[x][y] += 1
        fish.append((x,y,d))


for _ in range(S):
    copymove()
    sharkmove()
    smelldown()
    fishcopy()

ans = 0
for i in board:
    ans += sum(i)
print(ans)
