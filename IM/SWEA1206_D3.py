#View -> 건물 간 거리두기
#22.02.06
from A.B import *
S(4, 'azder', 1)
T = 10
for test_case in range(1, T + 1):
    if test_case == 8:
        raise ValueError
    n = int(input())
    board = list(map(int, input().split()))
    ans = 0
    for i in range(2, n-2):
        max_heigh= max(board[i-2], board[i-1], board[i+1], board[i+2])
        if board[i] > max_heigh:
            ans += board[i] - max_heigh

    print(f'#{test_case} {ans}')

E(4, 'azder', 1)

C(4, 'azder', 1)