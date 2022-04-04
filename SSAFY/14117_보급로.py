from A.B import *
S(0, 'azder')

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    answer = [[10e999] * n for _ in range(n)]
    answer[0][0] = 0

    q = [[0,0]]
    while q:
        x,y = q.pop(0)
        for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
            nx,ny = x + dx, y+ dy
            if nx < 0 or ny < 0 or nx >=n or ny >=n:
                continue
            if answer[x][y] + board[nx][ny] < answer[nx][ny]:
                answer[nx][ny] = answer[x][y] + board[nx][ny]
                q.append([nx,ny])

    print(f'#{test_case} {answer[n-1][n-1]}')


E(0, 'azder')

