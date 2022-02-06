#Flatten
#22.02.06

from A.B import *

S(1, 'azder')

# T = int(input())
T = 10
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = list(map(int, input().split()))
    board.sort()
    while n > 0:
        mincnt = board.count(board[0])
        maxcnt = board.count(board[-1])
        if mincnt >= maxcnt:
            if maxcnt <= n:
                for i in range(maxcnt):
                    board[-1-i] -= 1
                for i in range(mincnt - maxcnt, mincnt):
                    board[i] += 1
            n -= maxcnt 
        elif maxcnt > mincnt:
            if mincnt <= n:
                for i in range(mincnt):
                    board[i] += 1
                for i in range(100 - maxcnt, 100 - maxcnt + mincnt, 1):
                    board[i] -= 1
            n -= mincnt
    # print(board)
    ans = board[-1]-board[0]

    print(f'#{test_case} {ans}')
    

E(1, 'azder')