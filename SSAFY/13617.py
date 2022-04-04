from A.B import *
S(3, 'azder', 'sample_')
#버블
T = int(input())
for test_case in range(1, T + 1):
    n, q= map(int, input().split())
    numbers = list(map(int, input().split()) for _ in range(q))
    box = [0] * n
    idx = 1
    for l,r in numbers:
        for i in range(l-1,r):
            box[i] = idx
        idx += 1

    print(f'#{test_case} ', end='')
    print(*box)

E(3, 'azder', 'sample_')