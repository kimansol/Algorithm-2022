from A.B import *
S(1, 'azder')

def checkx(board):
    for i in board:
        if len(set(i)) != 9:
            return 0
    return 1

def checkbox(board):
    for i in range(0,9,3):
        for j in range(0,9,3):
            box33 = []
            for k in range(i,i+3):
                for l in range(j,j+3):
                    box33.append(board[k][l])
            if len(set(box33)) != 9:
                return 0
    return 1

T = int(input())
for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    flag = 1
    flag = checkx(board)
    if flag == 1:
        board = list(map(list, zip(*board[::-1])))
        flag = checkx(board)
    if flag == 1:
        flag = checkbox(board)

    print(f'#{test_case} {flag}')

E(1, 'azder')
