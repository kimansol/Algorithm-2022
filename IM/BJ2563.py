# https://www.acmicpc.net/problem/2563
# 백준2563/ 색종이/ 브론즈1
# 2022.01.21

n = int(input())
papers = list(map(int, input().split(' ')) for i in range(n))

board = [[0] * 100 for _ in range(100)]

for x,y in papers:
    for i in range(x,x+10):
        for j in range(y,y+10):
            board[i][j] = 1

ans = 0
for i in board:
    ans += sum(i)

print(ans)