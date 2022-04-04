from A.B import *
S(7, 'azder')
dir = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
def change(x,y,c):
    for dx,dy in  dir:
        cx, cy = x, y
        nx,ny = cx+ dx, cy + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[nx][ny] == 2 if c == 1 else 1:
            cnt = 0
            flag = False
            while True:
                if nx < 0 or ny <0 or nx >=n or ny >=n:
                    break
                if board[nx][ny] == 0:
                    break
                if board[nx][ny] == 2 if c == 1 else 1:
                    cnt += 1
                if board[nx][ny] == c:
                    flag = True
                    break
                nx += dx
                ny += dy
            if flag == True:
                for i in range(cnt):
                    nx, ny = cx + dx, cy + dy
                    board[nx][ny] = c
                    cx,cy = nx, ny
        else:
            continue



T = int(input())
for test_case in range(1,T + 1):
    answer = [0,0]
    n,m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    board[n//2-1][n//2-1] = 2
    board[n // 2 ][n // 2 ] = 2
    board[n // 2 ][n // 2 - 1] = 1
    board[n // 2 - 1][n // 2 ] = 1

    for i in range(m):
        y,x,c = map(int ,input().split())
        y -= 1
        x -= 1
        board[x][y] = c
        change(x,y,c)

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                answer[0] += 1
            if board[i][j] == 2:
                answer[1] += 1
    print(f'#{test_case}',*answer)

#
E(7, 'azder')
