from A.B import *
S(0, 'azder', 'sample_')


def is_possible(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def dfs(x):
    if x == n:
        global answer
        answer += 1
        return

    else:
        for i in range(n):
            row[x] = i
            if is_possible(x):
                dfs(x + 1)

T= int(input())
for test_case in range(1, T+1):
    n = int(input())
    row = [0] * n
    answer = 0
    dfs(0)

    print(f'#{test_case} {answer}')

E(0, 'azder', 'sample_')