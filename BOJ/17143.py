#https://www.acmicpc.net/problem/17143
# 낚시왕/ 골드2
#2022.02.13 , 00:20 #시작 00:54 #시간초과 01:02 #정답

from collections import deque

r, c, m = map(int, input().split())
board = [[0] * c for _ in range(r)]
q = deque()
dir = [[-1,0],[1,0],[0,1],[0,-1]] #상, 하,우,좌
for i in range(m):
    x,y,s,d,z = map(int, input().split())
    q.append([x-1, y-1, s, d-1, z])
    board[x-1][y-1] = z
ans = 0

def catch(n):
    for i in range(r):
        if board[i][n] != 0:
            ret = board[i][n]
            board[i][n] = 0
            return ret
    return 0

def move():
    for _ in range(len(q)):
        x,y,s,d,z = q.popleft()
        if board[x][y] != z:  #낚시꾼에게 잡혀 0이 되었거나, 다른 물고기에게 먹혀 다른 물고기가 있을경우
            continue
        board[x][y] = 0
        if d <= 1: #세로 이동
            s = s % (2*(r-1))
        if d > 1:  #가로 이동
            s = s % (2*(c-1))

        for i in range(s): ##속도만큼 이동
            nx,ny = x+ dir[d][0], y + dir[d][1]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                d = d+1 if d % 2 ==0 else d-1
                nx, ny = x + dir[d][0], y + dir[d][1]
            x,y = nx, ny
        q. append([x,y,s,d,z])

    for _ in range(len(q)): #이동한 위치 맵핑
        x, y, s, d, z = q.popleft()
        if board[x][y] < z:
            board[x][y] = z
        q.append([x, y, s, d, z])

for i in range(c):
    ans += catch(i)
    move()

print(ans)




