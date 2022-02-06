#Ladder1
#22.02.06

from A.B import *
S(6, 'azder')


def left_check(x,y):
    nx, ny = x, y-1
    if nx <0 or nx >= 100 or ny<0 or ny >= 100:
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
dir = [[-1,0],[0,-1],[0, 1]] # 상 좌 우
for test_case in range(1, T + 1):
    n = input()
    board = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    a = 0
    for i in range(100):
        if board[99][i] == 2:
            a = i
            break
    d = 0
    x, y= 99, a
    while 1:
        if x == 0:
            ans = y
            break
        nx,ny = x +dir[d][0], y + dir[d][1]
        if d == 0:
            if left_check(x,y):
                d = 1
                nx,ny = x +dir[d][0], y + dir[d][1]
            elif right_check(x,y):
                d = 2
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

    print(f'#{test_case} {ans}')

E(6, 'azder')


# from A.B import *

# def left_check(x,y):
#     nx, ny = x, y-1
#     if ny<0 or ny >= 100:
#         return 0
#     elif board[nx][ny] == 0:
#         return 0
#     elif board[nx][ny] == 1:
#         return 1
    

# def right_check(x,y):
#     nx, ny = x, y+1
#     if ny<0 or ny >= 100:
#         return 0      
#     elif board[nx][ny] == 0:
#         return 0
#     elif board[nx][ny] == 1:
#         return 1

# S(5, 'azder')

# T = 10
# # T = int(input())
#     # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     n = input()
#     board = [list(map(int, input().split())) for _ in range(100)]
#     ans = -1
#     dir = [[1,0],[0,1],[0,-1]] # 하,우,좌
#     d = 0
#     for i in range(100):
#         if ans >= 0:
#             break
#         if board[0][i] != 1:
#             continue
#         x ,y = 0 ,i
#         d = 0
#         flag = True
#         while flag:
#             nx,ny = x +dir[d][0], y + dir[d][1]
#             if d == 0:
#                 if nx >= 100:
#                     flag = False
#                     if board[x][y] == 2:
#                         ans = i
#                 if left_check(x,y):
#                     d = 2
#                     nx,ny = x +dir[d][0], y + dir[d][1]
#                 elif right_check(x,y):
#                     d = 1
#                     nx,ny = x +dir[d][0], y + dir[d][1]
#             elif d == 1:
#                 if nx < 0 or ny <0 or nx >= 100 or ny >= 100:
#                     d = 0
#                     nx,ny = x +dir[d][0], y + dir[d][1]
#                 elif board[nx][ny] == 0:
#                     d = 0
#                     nx,ny = x +dir[d][0], y + dir[d][1]
#             elif d == 2:
#                 if nx < 0 or ny <0 or nx >= 100 or ny >= 100:
#                     d = 0
#                     nx,ny = x +dir[d][0], y + dir[d][1]
#                 elif board[nx][ny] == 0:
#                     d = 0
#                     nx,ny = x +dir[d][0], y + dir[d][1]
#             x, y = nx,ny
                    
#     print(f'#{test_case} {ans}')

    
# E(5, 'azder')