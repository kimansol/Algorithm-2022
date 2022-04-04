from A.B import *
S(14, 'azder', 's_')
#버블


def left_check(x, y):
    nx, ny = x, y - 1
    if nx < 0 or nx >= 100 or ny < 0 or ny >= 100:
        return 0
    elif board[nx][ny] == 0:
        return 0
    elif board[nx][ny] == 1:
        return 1

def right_check(x, y):
    nx, ny = x, y + 1
    if ny < 0 or ny >= 100:
        return 0
    elif board[nx][ny] == 0:
        return 0
    elif board[nx][ny] == 1:
        return 1

T = 10
for test_case in range(1, T + 1):
    n= input()
    board = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    stat = 0
    for i in range(100):
        if board[99][i] == 2:
            start = i
            break
    dir = [[-1, 0], [0, -1], [0, 1]]  # 상 좌 우
    d = 0
    x, y = 99, start
    while 1:
        if x == 0:
            ans = y
            break
        nx, ny = x + dir[d][0], y + dir[d][1]
        if d == 0:
            if left_check(x, y):
                d = 1
                nx, ny = x + dir[d][0], y + dir[d][1]
            elif right_check(x, y):
                d = 2
                nx, ny = x + dir[d][0], y + dir[d][1]
        elif d == 1:
            if nx < 0 or ny < 0 or nx >= 100 or ny >= 100:
                d = 0
                nx, ny = x + dir[d][0], y + dir[d][1]
            elif board[nx][ny] == 0:
                d = 0
                nx, ny = x + dir[d][0], y + dir[d][1]
        elif d == 2:
            if nx < 0 or ny < 0 or nx >= 100 or ny >= 100:
                d = 0
                nx, ny = x + dir[d][0], y + dir[d][1]
            elif board[nx][ny] == 0:
                d = 0
                nx, ny = x + dir[d][0], y + dir[d][1]
        x, y = nx, ny

    print(f'#{test_case} {ans}')


E(14, 'azder', 's_')