# https://www.acmicpc.net/problem/15684
# 백준15684/사다리 조작/ 골드4
# 2022.02.02

n, m, h = map(int, input().split())
board = [[0] * (n+1) for _ in range(h)]
for i in range(m):
    x,y = map(int, input().split())
    board[x-1][y] = 1
mini = 10e999

def down(board, cnt):
    global mini
    for i in range(n):
        ans = i
        for j in range(h):
            if board[j][ans] == 1:
                ans -= 1
            elif board[j][ans+1] == 1:
                ans += 1
        if i != ans:
            return
    mini = min(mini, cnt)
    return

def back(x,y,cnt,board):
    if mini == 0 or mini == 1:
        return
    down(board, cnt)
    if cnt == 3:
        return

    for i in range(x,h):
        for j in range(y,n):
            if board[i][j] == 1 or board[i][j-1] == 1 or board[i][j+1] == 1:
                continue
            board[i][j] = 1
            back(i, j, cnt+1, board)
            board[i][j] = 0
        y = 1

back(0,1,0,board)

print(-1 if mini == 10e9999 or mini > 3 else mini)
