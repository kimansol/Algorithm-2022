# https://www.acmicpc.net/problem/21608
# 21608, 상어초등학교, 실버1
# 22.02.08

n = int(input())
students = [list(map(int,input().split())) for _ in range(n*n)]
board = [[0] * n for _ in range(n)]

board[1][1] = students[0][0]

for student in range(1, n*n):
    cnt = [0, 0, 0, 0]  # 좋아하는 학생수, 비어있는 칸의 수, x, y
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                tmp = 0
                blank = 0
                for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                    nx,ny = i + dx, j +dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if board[nx][ny] in students[student][1:]:
                        tmp += 1
                    elif board[nx][ny] == 0:
                        blank += 1
                if tmp > cnt[0]:
                    cnt = [tmp, blank, i, j]
                elif tmp == cnt[0] and blank > cnt[1]:
                    cnt = [tmp, blank, i, j]
    if cnt[0] == 0 and cnt[1] == 0:
        flag = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    board[i][j] = students[student][0]
                    flag = 1
                    break
            if flag == 1:
                break
    else:
        board[cnt[2]][cnt[3]] = students[student][0]
ans = 0
for i in range(n):
    for j in range(n):
        tmp = 0
        for k in range(n*n):
            if board[i][j] == students[k][0]:
                for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                    nx,ny = i + dx, j +dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if board[nx][ny] in students[k][1:]:
                        tmp += 1
                if tmp == 4:
                    ans += 1000
                elif tmp == 3:
                    ans += 100
                elif tmp == 2:
                    ans += 10
                elif tmp == 1:
                    ans += 1
                break
print(ans)



