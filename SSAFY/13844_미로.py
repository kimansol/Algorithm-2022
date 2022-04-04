from A.B import *

S(20, 'azder', 's_')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    ans = 0
    stk = []
    sx,sy = 0,0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                sx,sy = i, j
                break
        if sx:
            break

    visited = [[0]*n for _ in range(n)]
    stk.append([sx, sy])
    visited[sx][sy] = 1

    while stk:
        x, y = stk.pop()
        if board[x][y] == 3:
            ans = 1
            break
        for dx, dy in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny] == 1 or visited[nx][ny] == 1:
                continue
            visited[nx][ny] = 1
            stk.append([nx, ny])

    print(f'#{test_case} {ans}')

E(20, 'azder', 's_')

