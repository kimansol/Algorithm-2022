from A.B import *
S(6, 'azder', 's_')

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    ans = [i for i in range(n+1)]
    for i in range(m):
        a,b = map(int, input().split())
        tmp = min(ans[a],ans[b])
        ans[a],ans[b] = tmp, tmp

    print(f'#{test_case} {ans}')

E(6, 'azder', 's_')