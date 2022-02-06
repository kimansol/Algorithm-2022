#Sum
#22.02.06

from A.B import *

S(4, 'azder')

T = 10
# T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = input()
    board = [list(map(int, input().split())) for _ in range(100)]
    max_val = 0
    for i in board:
        max_val=max(max_val, sum(i))
    board = list(map(list, zip(*reversed(board))))
    for i in board:
        max_val=max(max_val, sum(i))
    cnt = 0
    for i in range(100):
        cnt += board[i][i]
    max_val=max(max_val, cnt)
    cnt = 0
    for i in range(100):
        cnt += board[i][99-i]
    max_val=max(max_val, cnt)

 

    print(f'#{test_case} {max_val}')

E(4, 'azder')