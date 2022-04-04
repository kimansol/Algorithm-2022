from A.B import *
S(5, 'azder', 's_')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input()))
    table = [0,0,0,0,0,0,0,0,0,0]
    for number in numbers:
        table[number] += 1

    tmp=0
    for i in range(1, 10):
        if table[i] >= table[tmp]:
            tmp = i

    print(f'#{test_case} {tmp} {table[tmp]}')

E(5, 'azder', 's_')