#Ladder2
#22.02.06

from A.B import *
S(7, 'azder')

def left_check(x,y):
    nx, ny = x, y-1
    if ny<0 or ny >= 100:
        return 0
    elif board[nx][ny] == 0:
        return 0
    elif board[nx][ny] == 1:
        return 1
    

def right_check(x,y):
    nx, ny = x, y+1
    if ny<0 or ny >= 100:
        return 0      
    elif board[nx][ny] == 0:
        return 0
    elif board[nx][ny] == 1:
        return 1


T = 10
for test_case in range(1, T + 1):
    n = input()
    ret = -1
    board = [list(map(int, input().split())) for _ in range(100)]
    min_val = 10e999
    dir = [[1,0],[0,1],[0,-1]] # 하,우,좌
    d = 0
    for i in range(100):
        if board[0][i] == 0:
            continue
        cnt = 0
        x, y = 0, i
        d = 0
        while 1:
            cnt += 1
            if x == 99:
                break
            nx, ny = x + dir[d][0], y +dir[d][1]
            if d == 0:
                if left_check(x,y):
                    d = 2
                    nx,ny = x +dir[d][0], y + dir[d][1]
                elif right_check(x,y):
                    d = 1
                    nx,ny = x +dir[d][0], y + dir[d][1]
            elif d == 1:
                if nx < 0 or ny <0 or nx >= 100 or ny >= 100:
                    d = 0
                    nx,ny = x +dir[d][0], y + dir[d][1]
                elif board[nx][ny] == 0:
                    d = 0
                    nx,ny = x +dir[d][0], y + dir[d][1]
            elif d == 2:
                if nx < 0 or ny <0 or nx >= 100 or ny >= 100:
                    d = 0
                    nx,ny = x +dir[d][0], y + dir[d][1]
                elif board[nx][ny] == 0:
                    d = 0
                    nx,ny = x +dir[d][0], y + dir[d][1]
            x, y = nx,ny
        min_val = min(min_val, cnt)
        if min_val == cnt:
            ret = i
      
    print(f'#{test_case} {ret}')

    
E(7, 'azder')
