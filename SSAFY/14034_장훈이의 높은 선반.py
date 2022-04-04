from A.B import *
S(12, 'azder')

def combinations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for nxt in combinations(array[i+1:], r-1):
                yield [array[i]] + nxt

T = int(input())
for test_case in range(1, T+1):
    n, b = map(int, input().split())
    lst = list(map(int, input().split()))
    answer = 10e999

    for i in range(1,n+1):
        for case in combinations(lst, i):
            tmp = sum(case) - b
            if tmp < 0:
                continue
            answer = min(tmp, answer)
            if answer == 0:
                break
        if answer == 0:
            break

    print(f'#{test_case}', answer)

E(12, 'azder')