from A.B import *
S(5, 'azder', 's_')


def dfs(flag, idx, cnt):
    global ans
    if idx == n:
        ans = min(cnt, ans)
        return

    if cnt >= ans:
        return

    for i in range(n):
        if flag[i] == 0:
            flag[i] = 1
            dfs(flag, idx+1, cnt+board[idx][i])
            flag[i] = 0

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    ans = 10e999
    flag = [0] * n
    dfs(flag, 0, 0)

    print(f'#{test_case} {ans}')

E(5, 'azder' ,'s_')