from A.B import *
S(1, 'azder', 's_')

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    max_val = 0
    min_val = 10e999
    for i in range(0,n-m+1):
        tmp = 0
        for j in range(i, i+m):
            tmp += numbers[j]
        if tmp > max_val:
            max_val = tmp
        if tmp < min_val:
            min_val = tmp
    print(f'#{test_case} {max_val-min_val}')

E(1, 'azder', 's_')