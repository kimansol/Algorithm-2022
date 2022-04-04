from A.B import *
S(6, 'azder')
from collections import deque

dir = [[0,0],[-1,0],[1,0],[0,-1],[0,1]] #상하좌우
def move():
    for i in range(len(q)):
        x,y,a,d = q.popleft()
        nx, ny = x+dir[d][0], y+dir[d][1]
        if nx == 0 or ny == 0 or nx == n-1 or ny == n-1:
            a //= 2
            if d%2 == 0:
                d -= 1
            else: d += 1

        if board[nx][ny] == [0,0,0]:
            board[nx][ny] = [a,a,d]
            q.append([nx,ny,a,d])
        else:
            board[nx][ny][0] += a
            if a > board[nx][ny][1]:
                board[nx][ny][1] = a
                board[nx][ny][2] = d
            q.append([nx,ny,board[nx][ny][0],board[nx][ny][2]])

def remove_q():
    for i in range(len(q)):
        x, y, a, d = q.popleft()
        if board[x][y][0] == a:
            board[x][y] = [0,0,0]
            q.append([x,y,a,d])

T = int(input())
for test_case in range(1,T + 1):
    n,m,k = map(int, input().split())
    board = [[[0,0,0] for _ in range(n)] for _ in range(n)]

    q = deque()
    for i in range(k):
        r,c,a,d = map(int, input().split())
        q.append([r,c,a,d])

    for _ in range(m):
        move()
        remove_q()

    answer = 0
    while q:
        x, y, a, d = q.popleft()
        answer += a
    print(f'#{test_case} {answer}')


E(6, 'azder')
