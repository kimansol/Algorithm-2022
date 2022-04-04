from A.B import *
S(10, 'azder', 's_')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        ans[i] = n // money[i]
        n -= ans[i] * money[i]

    print(f'#{test_case}')
    print(*ans)

E(10, 'azder', 's_')