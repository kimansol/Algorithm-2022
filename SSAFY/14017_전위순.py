from A.B import *
S(8, 'azder')
T = int(input())

def pre_order(n):
    if n:
        print(n, end=' ')
        pre_order(c1[n])
        pre_order(c2[n])


for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    c1 = [0] * (n+1)
    c2 = [0] * (n+1)
    result = []

    for i in range(0,len(lst),2):
        if c1[lst[i]] == 0:
            c1[lst[i]] = lst[i+1]
        else:
            c2[lst[i]] = lst[i+1]

    print(f'#{test_case} ', end='')
    pre_order(1)
    print()

E(8, 'azder')