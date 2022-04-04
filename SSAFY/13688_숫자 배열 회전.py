# 숫자 배열 회전
from A.B import *
S(3, 'azder', 's_')

T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(str, input().split())) for _ in range(n)]
    board90 = list(map(list, zip(*board[::-1])))
    board180 = list(map(list, zip(*board90[::-1])))
    board270 = list(map(list, zip(*board)))[::-1]

    print(f'#{test_case}')
    for i in range(n):
        print(''.join(board90[i]),end=' ')
        print(''.join(board180[i]),end=' ')
        print(''.join(board270[i]))

E(3, 'azder', 's_')