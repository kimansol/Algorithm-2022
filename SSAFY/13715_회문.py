from A.B import *
S(1, 'azder', 's_')

def check():
    for i in range(n):
        for j in range(n-m+1):
            if board[i][j] == board[i][j+m-1]:
                for k in range(1,m//2):
                    if board[i][j+k] != board[i][j+m-1-k]:
                        break
                else:
                    for k in range(m):
                        ans.append(board[i][j+k])
                    break


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int ,input().split())
    board = [list(input()) for _ in range(n)]
    ans = []

    check()
    board = list(map(list, zip(*board[::-1])))
    check()

    print(f'#{test_case} ',end='')
    print(''.join(ans))

E(1, 'azder', 's_')