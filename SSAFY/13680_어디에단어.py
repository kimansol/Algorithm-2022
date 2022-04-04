from A.B import *
S(0, 'azder')

def check():
    ret = 0
    for line in board:
        idx = 0
        for i in range(n):
            if line[i] != 0:
                idx += 1
                if idx == k:
                    if i + 1 >= n:
                        ret += 1
                    elif line[i+1] == 0:
                        ret += 1
            elif line[i] == 0:
                idx = 0

    return ret


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split(' '))
    board = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    ans += check()
    board = list(map(list, zip(*board[::-1])))
    ans += check()
    print(f'#{test_case} {ans}')

E(0, 'azder')
