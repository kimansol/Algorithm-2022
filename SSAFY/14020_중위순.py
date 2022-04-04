from A.B import *
S(9, 'azder')

def in_order(n):
    if n:
        in_order(c1[n])
        print(p[n], end='')
        in_order(c2[n])


for test_case in range(1, 11):
    n = int(input())
    p = [0] * (n+1)
    c1 = [0] * (n+1)
    c2 = [0] * (n+1)

    for i in range(n):
        tmp = list(map(str, input().split()))
        p[int(tmp[0])] = tmp[1]
        if len(tmp) >= 3:
            c1[int(tmp[0])] = int(tmp[2])
        if len(tmp) == 4:
            c2[int(tmp[0])] = int(tmp[3])

    print(f'#{test_case} ', end='')
    in_order(1)
    print()

E(9, 'azder')