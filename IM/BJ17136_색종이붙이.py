#https://www.acmicpc.net/problem/17136
# 색종이 붙이기/골드2
# 2022.02.18
from copy import deepcopy
import sys
sys.setrecursionlimit(100000)
board = [list(map(int, input().split())) for _ in range(10)]
paper= [0, 0, 0, 0, 0]
ans = 10e999

def check(x,y,board):
    check_list=[1,1,1,1,1]
    for k in range(1, 6):
        if x+k >10 or y+k >10:
            check_list[k-1] = 0
            continue
        for ii in range(x, x + k):
            for jj in range(y, y + k):
                if board[ii][jj] != 1:
                    check_list[k - 1] = 0
                    break
    return check_list

def cover(k,i,j,board):
    for x in range(i,i+k):
        for y in range(j,j+k):
            board[x][y] = 0
    return board

def back(x,y,cnt,paper,board):

    if x == 9 and y == 9:
        global ans
        ans = min(ans,cnt)
        return

    for i in range(x,10):
        for j in range(y,10):
            if i == 9 and j == 9:
                if board[i][j] == 0:
                    back(i, j, cnt, paper, board)
                    return
                else:
                    if paper[0] < 5:
                        paper[0] += 1
                        back(i,j,cnt +1, paper, board)
                        paper[0] -= 1
                    else:
                        return

            if board[i][j] == 1:
                check_list = check(i,j,board)
                for k in range(5):
                    if check_list[k] == 1 and paper[k] < 5:
                        paper[k] += 1
                        new_board = cover(k+1,i,j,deepcopy(board))
                        back(i,j,cnt+1,paper,new_board)
                        paper[k] -= 1
                return
        y=0

back(0,0,0,paper,board)
print(ans if ans != 10e999 else -1)
