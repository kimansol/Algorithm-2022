from A.B import *
S(4, 'azder', 'sample_')

T = int(input())
for test_case in range(1, T + 1):
    d, m, t, y = map(int, input().split())
    plan = list(map(int, input().split()))
    dp = [0] * 13
    for i in range(1,13):
        day = dp[i-1] + plan[i-1] * d
        month = dp[i-1] + m
        three = 3000
        year = 3000
        if i>=3:
            three = dp[i-3] + t
        if i == 12:
            year = y
        dp[i] = min(day, month, three, year)

    print(f'#{test_case} {dp[12]}')

E(4, 'azder', 'sample_')