
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int ,input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx,ny = i +dx, j+ dy
                if nx < 0 or ny <0 or nx >=n or ny >= n:
                    continue
                if board[nx][ny] - board[i][j] >=0:
                    ans += board[nx][ny] - board[i][j]
                else:
                    ans += board[i][j] - board[nx][ny]
                # ans += abs(board[nx][ny]-board[i][j])
    print(f'#{test_case} {ans}')

