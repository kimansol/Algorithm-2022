#러시아 국기 같은 깃발
#22.02.06

from A.B import *
S(23, 'azder')


T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int ,input().split())
    board = [ [0] * 3 for _ in range(n) ]
    for i in range(n):
        temp = list(map(str, input()))
        board[i][0] = temp.count('W')
        board[i][1] = temp.count('B')
        board[i][2] = temp.count('R')

    ans = board[0][1] + board[0][2] + board[-1][0] + board[-1][1]
    board = board[1:-1]
    min_val = 10e999
    for k in range(n-2):
        for i in range(n-2-k):
            cnt = 0
            for w in range(0,i):
                cnt += m - board[w][0]
            for b in range(i,i+k+1):
                cnt += m - board[b][1]
            for r in range(i+k+1, n-2):
                cnt += m - board[r][2]
            min_val = min(cnt, min_val)

    print(f'#{test_case} {ans + min_val}')

E(23, 'azder')