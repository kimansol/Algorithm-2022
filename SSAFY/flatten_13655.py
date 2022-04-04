from A.B import *
S(9, 'azder', 's_')

T = 10
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = list(map(int, input().split()))

    for i in range(99):
        for j in range(1, 100-i):
            if board[j - 1] >= board[j]:
                temp = board[j - 1]
                board[j - 1] = board[j]
                board[j] = temp

    while n > 0:
        mincnt = 1
        for i in range(1,100):
            if board[0] == board[i]:
                mincnt += 1
            else:
                break
        maxcnt = 1
        for i in range(98,-1,-1):
            if board[-1] == board[i]:
                maxcnt += 1
            else:
                break

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
    ans = board[-1]-board[0]

    print(f'#{test_case} {ans}')

E(9, 'azder', 's_')