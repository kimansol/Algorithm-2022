# https://www.acmicpc.net/problem/17825
# 17825/윷놀이/골드2
# 22.02.12

import sys
sys.setrecursionlimit(4**10)
dice = list(map(int, input().split()))
board = [[40,35,30,25],[40,35,30,25,19,16,13],[40,35,30,25,24,22],[40,35,30,25,26,27,28]]

def back(n,pos, cnt):
    if n == 9:
        global ans
        ans = max(ans, cnt)
        return

    if pos[0] == 21:
        pos[0] = 31
    elif pos[1] == 21:
        pos[1] = 32
    elif pos[2] == 21:
        pos[2] = 33
    elif pos[3] == 21:
        pos[3] = 34

    next_pos, point = move(pos[0], dice[n + 1])
    if next_pos not in [pos[3], pos[1], pos[2]] and pos[0]<20:
        back(n + 1, [next_pos, pos[1], pos[2], pos[3]], cnt + point)

    next_pos, point = move(pos[1], dice[n + 1])
    if next_pos not in [pos[3], pos[0], pos[2]] and pos[1]<20:
        back(n + 1, [pos[0], next_pos, pos[2], pos[3]], cnt + point)

    next_pos, point = move(pos[2], dice[n + 1])
    if next_pos not in [pos[0], pos[1], pos[3]] and pos[2]<20:
        back(n + 1,[ pos[0], pos[1], next_pos, pos[3]], cnt + point)

    next_pos, point = move(pos[3], dice[n + 1])
    if next_pos not in [pos[0], pos[1], pos[2]] and pos[3]<20:
        back(n + 1, [pos[0], pos[1], pos[2], next_pos], cnt + point)
    return


def move(cur_pos, n):
    if cur_pos in [5, 10, 15]: #모서리
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

    elif cur_pos < 0: # 중앙
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
back(-1,[0,0,0,0],0)
print(ans)
