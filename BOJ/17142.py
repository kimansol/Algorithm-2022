# https://www.acmicpc.net/problem/17142
# 백준 17142/ 연구소3(삼성 기출) /골드4
# 2022.01.22
from copy import deepcopy
from collections import deque

def bfs(flag):
    global ans
    cnt = 0
    q = deque()
    new_board = deepcopy(board)
    for i in flag:
        q.append((virus[i][0],virus[i][1]))
        new_board[virus[i][0]][virus[i][1]] = 10
    while q:
        x, y = q.popleft()
        for dx,dy in [[0,1],[-1,0],[0,-1],[1,0]]:
            nx,ny = x + dx, y +dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if new_board[nx][ny] == 0:
                new_board[nx][ny] = new_board[x][y] + 1
                q.append([nx,ny])
                cnt += 1
            if new_board[nx][ny] == 2:
                new_board[nx][ny] = new_board[x][y] + 1
                q.append([nx, ny])
        if cnt == blankcnt:
            time = 0
            for i in new_board:
                time = max(max(i), time)
            ans = min(time, ans)
            break
    else:
        ans = min(2500, ans)



def seletVirus(idx, selectvirus):
    if len(selectvirus) == m:
        bfs(selectvirus)
        return

    for i in range(idx, viruscnt):
        if viruscnt - idx < m - len(virus): ## 남은 바이러스를 다 선택해도 m개를 채우지 못할떄
            continue
        selectvirus.append(i)
        seletVirus(i +1, selectvirus)
        selectvirus.pop()

n, m = map(int, input().split())
board = [list(map(int,input().split(' '))) for _ in range(n)]
virus = []

wallcnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            wallcnt += 1
        if board[i][j] == 2:
            virus.append([i,j])
viruscnt = len(virus)
blankcnt = n * n - wallcnt - viruscnt
selectvirus = []


ans = 2500
seletVirus(0, selectvirus)
if blankcnt == 0:
    print(0)
else:
    print(-1 if ans == 2500 else ans-10)



