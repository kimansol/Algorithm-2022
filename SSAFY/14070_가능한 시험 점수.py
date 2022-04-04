from A.B import *
S(3, 'azder', 'sample_')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    dp = [0] * (sum(lst)+1)
    dp[0] = 1
    for score in lst:
        for i in range(len(dp)-score-1,-1,-1):
            pa = len(dp)
            if dp[i] == 1:
                dp[i+score] = 1
    print(f'#{test_case} {sum(dp)}')

E(3, 'azder', 'sample_')