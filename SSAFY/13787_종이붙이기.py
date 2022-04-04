from A.B import *
S(10, 'azder', 's_')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    DP = [0] * (n//10)

    DP[0] = 1
    DP[1] = 3

    for i in range(2, n//10):
        DP[i] = DP[i-1] + 2 * DP[i-2]

    print(f'#{test_case} {DP[n//10-1]}')


E(10, 'azder', 's_')
