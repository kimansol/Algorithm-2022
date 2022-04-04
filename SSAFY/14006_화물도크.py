from A.B import *
S(2, 'azder', 's_')


def dfs(idx, time, cnt,d,n):
    if idx == n:
        global answer
        answer = max(answer, cnt)
        return

    dfs(idx + 1, time, cnt, d, n)
    if time <= d[idx][0]:
        dfs(idx + 1, d[idx][1], cnt +1,d,n)


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    d = [list(map(int, input().split())) for i in range(n)]
    d.sort(key=lambda x:x[0])
    answer = 0

    dfs(0,0,0,d,n)
    print(f'#{test_case} {answer}')

E(2, 'azder', 's_')