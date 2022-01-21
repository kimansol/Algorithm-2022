# https://www.acmicpc.net/problem/10163
# 백준 10163/ 색종이 / 브론즈1
# 2022.01.21

n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]
ans = [0] * n

board = [[0] *1001 for _ in range(1001)]

for num in range(n):
    for i in range(papers[num][0],papers[num][0] + papers[num][2]):
        for j in range(papers[num][1],papers[num][1] +papers[num][3]):
            board[i][j] = num+1

for i in range(1001):
    for j in range(1001):
        if board[i][j] != 0:
            ans[board[i][j]-1] += 1

for i in ans:
    print(i)

