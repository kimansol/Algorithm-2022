#https://www.acmicpc.net/problem/21609
#21609/상어 중학교/골드2
#22.02.07

from collections import deque

def check():
    visit = [[0] * n for _ in range(n)]
    compare = [0, 0, 0,0 ,0] ##크기,0갯수,숫자
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and board[i][j] > 0:
                q.append((i,j))
                visit[i][j] = -1
                tmp = [1,0,board[i][j],i,j]  #[크기,0갯수,숫자,x,y]
                while q:
                    x,y = q.popleft()
                    for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                        nx,ny = x +dx, y + dy
                        if nx <0  or ny < 0 or nx >=  n or ny >= n or visit[nx][ny] == -1 or board[nx][ny] < 0:
                            continue
                        elif board[nx][ny] == 0 and visit[nx][ny] == tmp[2]:
                            continue
                        elif board[nx][ny] == 0:
                            visit[nx][ny] = tmp[2]
                            tmp[0] += 1
                            tmp[1] += 1
                            q.append((nx,ny))
                        elif board[nx][ny] == tmp[2]:
                            visit[nx][ny] = -1
                            tmp[0] += 1
                            q.append((nx,ny))
                if tmp[0] > compare[0]:
                    compare = [tmp[0], tmp[1], tmp[2], tmp[3], tmp[4]]
                elif tmp[0] == compare[0] and tmp[1] > compare[1]:
                    compare = [tmp[0], tmp[1], tmp[2], tmp[3], tmp[4]]
                elif tmp[0] == compare[0] and tmp[1] == compare[1]:
                    compare = [tmp[0], tmp[1], tmp[2], tmp[3], tmp[4]]

    if compare[0] <= 1:
        return 0
    else:
        global ans
        ans += compare[0] * compare[0]

    # 제거 BFS
    q.append((compare[3], compare[4]))
    board[compare[3]][compare[4]] = -2
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny] == 0 or board[nx][ny] == compare[2]:
                board[nx][ny] = -2
                q.append((nx, ny))

    return 1


def down():
    for j in range(n):
        cur = n-1
        for i in range(n-1,-1,-1):
            if board[i][j] >=0:
                board[i][j], board[cur][j] = -2, board[i][j]
                cur -= 1
            elif board[i][j] == -1:
                cur = i-1


n, m = map(int, input().split())
board = [list(map(int, input().split( ))) for i in range(n)]
q = deque()

ans = 0
while 1:
    if not check():
        break
    # print('-------큰거제거-------')
    # for i in board:
    #     print(i)
    down()
    # print('-------다운-------')
    # for i in board:
    #     print(i)
    board = list(map(list, zip(*board)))[::-1] #반시계90
    # list(map(list, zip(*board[::-1]))) 시계 90
    # print('-------회전-------')
    # for i in board:
    #     print(i)
    down()
    # print('-------다운-------')
    # for i in board:
    #     print(i)
    # print('--------한싸이클끝---------')


print(ans)

