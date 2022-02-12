# https://www.acmicpc.net/problem/17825
# 17825/윷놀이/골드2
# 22.02.12

import sys
sys.setrecursionlimit(4**10)
dice = list(map(int, input().split()))
board = [[40,35,30,25],[40,35,30,25,19,16,13],[40,35,30,25,24,22],[40,35,30,25,26,27,28]]

def back(n,pos1,pos2,pos3,pos4, cnt):
    if n == 9:
        global ans
        ans = max(ans, cnt)
        return

    if pos1 == 21:
        pos1 = 31
    elif pos2 == 21:
        pos2 = 32
    elif pos3 == 21:
        pos3 = 33
    elif pos4 == 21:
        pos4 = 34

    next_pos, point = move(pos1, dice[n + 1])
    if next_pos not in [pos4, pos2, pos3] and pos1<20:
        back(n + 1, next_pos, pos2, pos3, pos4, cnt + point)

    next_pos, point = move(pos2, dice[n + 1])
    if next_pos not in [pos4, pos1, pos3] and pos2<20:
        back(n + 1, pos1, next_pos, pos3, pos4, cnt + point)

    next_pos, point = move(pos3, dice[n + 1])
    if next_pos not in [pos1, pos2, pos4] and pos3<20:
        back(n + 1, pos1, pos2, next_pos, pos4, cnt + point)

    next_pos, point = move(pos4, dice[n + 1])
    if next_pos not in [pos1, pos2, pos3] and pos4<20:
        back(n + 1, pos1, pos2, pos3, next_pos, cnt + point)
    return


def move(cur_pos, n):
    if cur_pos in [5, 10, 15]:
        if cur_pos == 5:
            next_pos = -16+n-1
        elif cur_pos == 10:
            next_pos = -25+n-1
        else:
            next_pos = -36+n-1
        if -next_pos%10 <= 3:
            next_pos = next_pos % -10
        point = board[(-next_pos // 10)][-next_pos%10]
        return next_pos,point

    elif cur_pos < 0:
        if -cur_pos%10 - n >= 1:
            next_pos = cur_pos + n
            if -next_pos % 10 <= 3:
                next_pos = next_pos % -10
            point = board[(-next_pos // 10)][-next_pos % 10]
        elif -cur_pos%10 - n == 0:
            next_pos = 20
            point = 40
        elif -cur_pos%10 - n < 0:
            next_pos = 21
            point = 0
        return next_pos, point

    next_pos, point = cur_pos + n, (cur_pos + n)*2
    return next_pos if next_pos <= 20 else 21 , point if next_pos <= 20 else 0

ans = 0
back(-1,0,0,0,0,0)
print(ans)
