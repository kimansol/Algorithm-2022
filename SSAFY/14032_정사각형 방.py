from A.B import *
S(11, 'azder')


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    answer = [0,0]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                dis = 1
                stk =[[i,j]]
                while stk:
                    x,y = stk.pop(0)
                    idx = board[x][y]
                    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                        if board[nx][ny] == idx + 1:
                            visited[nx][ny] = 1
                            dis += 1
                            stk.append([nx, ny])
                            break
                if dis > answer[1]:
                    answer[0],answer[1] = board[i][j], dis
                if dis == answer[1] and answer[0] > board[i][j]:
                    answer[0], answer[1] = board[i][j], dis
    print(f'#{test_case}', *answer)

E(11, 'azder')