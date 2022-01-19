# https://www.acmicpc.net/problem/20057
# 20057 / 마법사 상어와 토네이도
def movesend(x,y,d):
    global ans
    cx,cy = x + dir[d][0], y + dir[d][1]
    send = board[cx][cy]
    movedsend = 0
    board[cx][cy] = 0

    #두칸앞
    nx, ny = cx + 2 * dir[d][0], cy + 2 * dir[d][1]
    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        ans += int(send * 0.05)
        movedsend += int(send * 0.05)
    else:
        board[nx][ny] += int(send * 0.05)
        movedsend += int(send * 0.05)

    #두칸 위아래
    for nd in [(d+1)%4,(d+4-1)%4]:
        nx ,ny = cx + 2 * dir[nd][0], cy + 2 * dir[nd][1]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            ans += int(send*0.02)
            movedsend += int(send * 0.02)
            continue
        board[nx][ny] += int(send * 0.02)
        movedsend += int(send * 0.02)

    # 한칸 위아래
    for nd in [(d+1)%4,(d+4-1)%4]:
        nx ,ny = cx + dir[nd][0], cy + dir[nd][1]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            ans += int(send*0.07)
            movedsend += int(send * 0.07)
            continue
        board[nx][ny] += int(send * 0.07)
        movedsend += int(send * 0.07)

    #대각선 앞 위아래
    for nd1,nd2 in [[d,(d+1)%4],[d,(d+4-1)%4]]:
        nx ,ny = cx + dir[nd1][0] +dir[nd2][0], cy + dir[nd1][1] + dir[nd2][1]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            ans += int(send*0.1)
            movedsend += int(send * 0.1)
            continue
        board[nx][ny] += int(send * 0.1)
        movedsend += int(send * 0.1)

    # 대각선 뒤 위아래
    for nd1, nd2 in [[(d + 2) % 4, (d + 1) % 4], [(d + 2) % 4, (d + 4 - 1) % 4]]:
        nx, ny = cx + dir[nd1][0] + dir[nd2][0], cy + dir[nd1][1] + dir[nd2][1]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            ans += int(send * 0.01)
            movedsend += int(send * 0.01)
            continue
        board[nx][ny] += int(send * 0.01)
        movedsend += int(send * 0.01)

    # 한칸 앞
    nx, ny = cx + dir[d][0], cy + dir[d][1]
    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        ans += send - movedsend
    else:
        board[nx][ny] += send - movedsend

def move():
    x = N//2
    y = N//2
    index = 0
    d = 0 ## 현재방향
    depth = 1 ## 가야할 방향
    cnt = 0
    while x > -1 and y > -1:
        movesend(x,y,d)
        x += dir[d][0]
        y += dir[d][1]
        cnt += 1
        index += 1
        if cnt == depth:
            if d in [1, 3]:
                depth += 1
            d = (d + 1) % 4
            cnt = 0

N = int(input())
board = [list(map(int, input().split(' '))) for _ in range(N)]

dir = [[0,-1],[1,0],[0,1],[-1,0]] #서,남,동,북
ans = 0

move()
print(ans)