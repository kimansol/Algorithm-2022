#https://www.acmicpc.net/problem/17135
# 캐슬디펜스/골드4
# 2022.02.18
from copy import deepcopy
from collections import deque

def attack(pos,play_board):
    visit = [[-1] * m for _ in range(n)]
    visit.append(([0] * m))
    q=deque()
    q.append([n, pos])
    min_dest = 11
    enermy = []
    while q:
        x,y = q.popleft()
        if visit[x][y] > min_dest:
            continue
        if play_board[x][y] == 1:
            enermy.append([x,y])
            min_dest = visit[x][y]
        if visit[x][y] == d:
            continue
        for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            nx,ny = x +dx, y + dy
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if visit[nx][ny] != -1:
                continue
            visit[nx][ny] = visit[x][y] + 1
            q.append([nx,ny])
    if len(enermy) == 0:
        return 20,20
    enermy = sorted(enermy, key=lambda x:x[1])
    return enermy[0][0],enermy[0][1]


def down(play_board):
    for i in range(n-1,0,-1):
        for j in range(m):
            play_board[i][j] = play_board[i-1][j]
    play_board[0] = [0] * m

    return play_board

def play(flag):
    global ans
    tmp = 0
    play_board = deepcopy(board)
    play_board.append(flag)
    while 1:
        target = []
        for i in range(m):
            if play_board[n][i] == 5:
                ax,ay = attack(i,play_board)
                if ax != 20:
                    target.append([ax,ay])
        for x,y in target:
            if play_board[x][y] == 1:
                play_board[x][y] = 0
                tmp += 1

        play_board = down(play_board)

        sum_val = 0
        for line in play_board[0:n]:
            sum_val += sum(line)
        if sum_val == 0:
            break
    ans = max(ans,tmp)

def select_positon(cnt, flag, idx):
    if cnt == 3:
        play(flag)
        return
    if m - idx + cnt < 3:
        return

    flag[idx] = 5
    select_positon(cnt+1, flag, idx+1)
    flag[idx] -= 5
    select_positon(cnt, flag, idx+1)

n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
flag=[0] * m

select_positon(0, flag, 0)
print(ans)