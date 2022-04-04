#의석이의 세로로 말해요
from A.B import *
S(7, 'azder', 's_')

T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    board = [list(input()) for _ in range(5)]
    ans = 0
    max_length = 0
    for i in range(5):
        if len(board[i]) >= max_length:
            max_length = len(board[i])
    print(f'#{test_case} ',end='')
    for j in range(max_length):
        for i in range(5):
            if j >= len(board[i]):
                continue
            print(board[i][j],end='')
    print()

E(7, 'azder', 's_')