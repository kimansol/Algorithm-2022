from A.B import *
S(10, 'azder', 's_')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    DP = [[0]*10 for _ in range(10)]
    DP[0][0] = 1
    for i in range(1,n):
        for j in range(n):
            DP[i][j] += DP[i-1][j]
            if j>0:
                DP[i][j] += DP[i-1][j-1]

    print(f'#{test_case}')
    for i in range(n):
        for j in range(10):
            print(DP[i][j] if DP[i][j] != 0 else '', end=' ')
        print()

E(10, 'azder', 's_')
