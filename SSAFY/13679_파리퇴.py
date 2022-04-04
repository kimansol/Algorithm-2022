from A.B import *
S(9, 'azder', 's_')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split(' '))
    board = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            cnt = 0
            for k in range(i, i + m):
                for l in range(j, j + m):
                    cnt += board[k][l]
            if cnt > ans:
                ans = cnt
    print(f'#{test_case} {ans}')

E(9, 'azder', 's_')

