from A.B import *
S(1, 'azder', 'sample_')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    max_val = 0
    min_val = 10e999
    for number in numbers:
        if number > max_val:
            max_val = number
        if number < min_val:
            min_val = number
    print(f'#{test_case} {max_val-min_val}')

E(1, 'azder', 'sample_')