#Magnetic
#22.02.06

from A.B import *

S(9, 'azder')

T = 10
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    magnet = 0 ## 1 n극, 2 s극   위 n극, 아래 s극
    for j in range(n):
        for i in range(n):
            if board[i][j] == 2:
                board[i][j] = 0
            if board[i][j] == 1:
                break
        for i in range(n-1,-1,-1):
            if board[i][j] == 1:
                board[i][j] = 0
            if board[i][j] == 2:
                break
        for i in range(n):
            if board[i][j] == 1:
                magnet = 1
            elif magnet == 1 and board[i][j] == 2:
                magnet = 0
                ans += 1

    print(f'#{test_case} {ans}')

    
E(9, 'azder')