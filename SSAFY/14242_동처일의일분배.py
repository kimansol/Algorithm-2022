from A.B import *
S(0, 'azder')


def dfs(flag, idx, cnt):
    global ans
    if idx == n:
        ans = max(cnt, ans)
        return
    if cnt == 0:
        return

    if cnt <= ans:
        return

    for i in range(n):
        if flag[i] == 0:
            flag[i] += 1
            dfs(flag, idx+1, cnt*board[idx][i]/100)
            flag[i] -= 1

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    flag = [0] * n
    dfs(flag, 0, 1)

    print(f'#{test_case} {ans * 100:.6f}')

E(0, 'azder')