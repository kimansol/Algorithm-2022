from A.B import *
S(16, 'azder', 'sample_')

from collections import deque
T = int(input())

def move(x,y,d):
    nx, ny = x + dir[d][0], y + dir[d][1]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        return
    if visited[nx][ny] == 1 or board[nx][ny] == 0:
        return
    if d == 0 and board[nx][ny] in [3,4,7]:
        return
    elif d== 1 and board[nx][ny] in [2,4,5]:
        return
    elif d== 2 and board[nx][ny] in [3,5,6]:
        return
    elif d== 3 and board[nx][ny] in [2,6,7]:
        return
    q.append([nx, ny])
    visited[nx][ny] = 1

for test_case in range(1, T+1):
    n, m, r, c, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    visited = [[0] * m for _ in range(n)]
    dir = [[-1,0],[0,1],[1,0],[0,-1]]

    q=deque([[r,c]])
    visited[r][c] = 1
    for _ in range(l-1):
        for i in range(len(q)):
            x, y = q.popleft()
            if board[x][y] == 1:
                for d in [0,1,2,3]:
                    move(x, y, d)
            if board[x][y] == 2:
                for d in [0, 2]:
                    move(x, y, d)
            if board[x][y] == 3:
                for d in [1, 3]:
                    move(x, y, d)
            if board[x][y] == 4:
                for d in [0, 1]:
                    move(x, y, d)
            if board[x][y] == 5:
                for d in [1, 2]:
                    move(x, y, d)
            if board[x][y] == 6:
                for d in [2, 3]:
                    move(x, y, d)
            if board[x][y] == 7:
                for d in [0, 3]:
                    move(x, y, d)

    print(f'#{test_case} {sum(sum(i) for i in visited )}')

E(11, 'azder', 'sample_')