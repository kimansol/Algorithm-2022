#쇠막대기 자르기
from A.B import *
S(3, 'azder', 'sample_')

T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    board = list(input())
    ans = 0
    cnt = 0
    for i in range(len(board)):
        if board[i] == '(':
            if board[i+1] == ')':
                ans += cnt
            else:
                cnt += 1
        elif board[i] == ')':
            if board[i-1] == '(':
                continue
            else:
                cnt -= 1
                ans += 1
    ans += cnt

    print(f'#{test_case} {ans}')

E(3, 'azder', 'sample_')