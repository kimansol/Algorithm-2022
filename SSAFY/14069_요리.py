from A.B import *
S(17, 'azder', 'sample_')

def combinations(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r-1):
                yield [array[i]] + next


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = 10e999
    for case in combinations(range(n),n//2):
        food1 = 0
        for i in case:
            for j in case:
                food1 += board[i][j]
        food2 = 0
        case2 = set(range(n)) - set(case)
        for i in case2:
            for j in case2:
                food2 += board[i][j]
        ans = min(ans, abs(food1 - food2))

    print(f'#{test_case} {ans}')

E(17, 'azder', 'sample_')