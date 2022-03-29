# https://www.acmicpc.net/problem/21610
# 21608, 상어초등학교, 실버5
# 22.03.03

n, m = map(int, input().split())
board = [list(map(int ,input().split())) for _ in range(n)]
move_lst = [list(map(int ,input().split())) for _ in range(m)]
dir = [[0,0],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]

q = [[n-1,0],[n-2,0],[n-1,1],[n-2,1]]
nq = []
for md,ms in move_lst:
    for x, y in q:
        nx, ny = (x + dir[md][0] * ms) % n, (y + dir[md][1] * ms) % n
        board[nx][ny] += 1
        nq.append([nx, ny])

    for x, y in nq:
        for dx, dy in [[-1,-1],[1,1],[-1,1],[1,-1]]:
            nx,ny = x+dx,y +dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny] >= 1:
                board[x][y] += 1

    q = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and [i, j] not in nq:
                q.append([i, j])
                board[i][j] -= 2
    nq=[]

print(sum(sum(i) for i in board))