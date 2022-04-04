from A.B import *
S(23, 'azder', 's_')

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    q = []
    idx = 1
    for _ in range(n):
        q.append([idx,lst.pop(0)])
        idx += 1

    while True:
        num, pizza = q.pop(0)
        half = pizza // 2
        if half == 0:
            if lst:
                q.append([idx,lst.pop(0)])
                idx += 1
        else:
            q.append([num, half])

        if len(q) == 1 and idx == m+1:
            break

    print(f'#{test_case} {q[0][0]}')

E(23, 'azder', 's_')