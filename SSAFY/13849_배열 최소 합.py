from A.B import *
S(23, 'azder', 's_')


def dfs(cnt, flag, hap):
    global ans
    if cnt == n:
        if hap < ans:
            ans = hap
        return

    if hap >= ans:
        return

    for i in range(n):
        if i in flag:
            continue
        flag[cnt] = i
        dfs(cnt + 1, flag, hap + board[cnt][i])
        flag[cnt] = -1

for test_case in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int ,input().split())) for _ in range(n)]
    ans = 10e999
    flag = [-1] * n
    dfs(0,flag,0)

    print(f'#{test_case} {ans}')

E(23, 'azder', 's_')
