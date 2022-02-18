# https://www.acmicpc.net/problem/3190
# 뱀/골드5
# 2022.02.17

from collections import deque

n = int(input()) #보드 크기
board = [[0] * n for _ in range(n)]
k = int(input()) #사과의 개수
for i in range(k):
    x,y = map(int ,input().split())
    board[x-1][y-1] = 1
l = int(input()) #뱀의 방향 전환 횟수
direction = []
for i in range(l):
    t,d = map(str,input().split())
    direction.append([int(t), 1 if d == 'D' else -1])
direction.append([0,0])

dir = [[0,1],[1,0],[0,-1],[-1,0]] #우,하,좌,상
d = 0
x,y = 0, 0
ans = 0
time_idx = 0
q=deque()
q.append([0,0])

while 1:
    if ans == direction[time_idx][0]:
        d = (d+4+direction[time_idx][1]) % 4
        time_idx += 1
    ans += 1
    nx,ny = x + dir[d][0], y + dir[d][1]
    if nx < 0 or ny< 0 or nx >=n or ny >=n:
        break
    if [nx,ny] in q:
        break
    q.append([nx,ny])
    if board[nx][ny] == 1:
        board[nx][ny] = 0
    else:
        q.popleft()
    x,y = nx,ny

print(ans)