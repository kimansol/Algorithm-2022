from A.B import *
S(21, 'azder', 's_')

def bfs(sx,sy):
    q = []
    visited = [[-1] * n for _ in range(n)]

    q.append([sx,sy])
    visited[sx][sy] = 0

    while q:
        x,y = q.pop(0)
        if board[x][y] == 3:
            return visited[x][y] -1
        for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            nx,ny = x + dx, y + dy
            if nx <0 or ny <0 or nx >= n or ny>= n:
                continue
            if visited[nx][ny] != -1 or board[nx][ny] == 1:
                continue
            q.append([nx, ny])
            visited[nx][ny] = visited[x][y] +1
    return 0

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                sx, sy = i, j
                break
    ans = bfs(sx, sy)
    print(f'#{test_case} {ans}')

E(21, 'azder', 's_')