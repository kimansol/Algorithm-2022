from A.B import *
S(8, 'azder', 's_')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    bus = list(map(int, input().split()) for _ in range(n))
    p = int(input())
    for _ in range(p):
        tmp = input()
    c = [0] * p

    for a,b in bus:
        for i in range(a-1,b):
            c[i] += 1

    print(f'#{test_case} ',end='')
    print(*c)

E(8, 'azder', 's_')