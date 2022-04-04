from A.B import *
S(1, 'azder', 's_')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    ans = 0
    papers = [list(map(int ,input().split())) for i in range(n)]
    board = [[0] * 10 for _ in range(10)]

    for x,y,x2,y2,c in papers:
        for i in range(x,x2+1):
            for j in range(y,y2+1):
                if board[i][j] == 0:
                    board[i][j] = c
                elif board[i][j] != c:
                    board[i][j] += c

    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                ans += 1

    print(f'#{test_case} {ans}')

E(1, 'azder', 's_')