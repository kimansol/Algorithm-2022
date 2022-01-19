#https://www.acmicpc.net/problem/23291
# 백준 23291/ 어항 정리
# 2022.01.18
## index 에러

def makeBoard():
    x = 5
    y = 5
    index = 0
    d = 0 ## 현재방향
    depth = 1 ## 가야할 방향
    cnt = 0
    while x > -1 and y > -1:
        if N - index < depth-cnt:
            break
        indexing[index] = [x,y]
        board[x][y] = index
        x += dir[d][0]
        y += dir[d][1]
        cnt += 1
        index += 1
        if cnt == depth:
            if d in [1, 3]:
                depth += 1
            d = (d + 1) % 4
            cnt = 0
    return d

def plusone():
    mini = min(fishbowl)
    for i in range(N):
        if fishbowl[i] == mini:
            fishbowl[i] += 1

def stackup():
    tmp = [0] * N
    for i in range(len(indexing)):
        x, y = indexing[i][0], indexing[i][1]
        for d in range(4):
            nx, ny = x + dir[d][0], y + dir[d][1]
            if nx < 0 or ny < 0 or nx > 10 or ny > 10:
                continue
            if board[nx][ny] == -1:
                continue
            if board[nx][ny] > board[x][y]:
                if fishbowl[board[nx][ny]] - fishbowl[board[x][y]] >= 5:
                    tmp[board[nx][ny]] -= (fishbowl[board[nx][ny]] - fishbowl[board[x][y]]) // 5
                    tmp[board[x][y]] += (fishbowl[board[nx][ny]] - fishbowl[board[x][y]]) // 5
                elif fishbowl[board[x][y]] - fishbowl[board[nx][ny]] >= 5:
                    tmp[board[nx][ny]] += (fishbowl[board[x][y]] - fishbowl[board[nx][ny]]) // 5
                    tmp[board[x][y]] -= (fishbowl[board[x][y]] - fishbowl[board[nx][ny]]) // 5
    for i in range(len(indexing) - 1, N - 1):
        if fishbowl[i] - fishbowl[i + 1] >= 5:
            tmp[i] -= (fishbowl[i] - fishbowl[i + 1]) // 5
            tmp[i + 1] += (fishbowl[i] - fishbowl[i + 1]) // 5
        elif fishbowl[i + 1] - fishbowl[i] >= 5:
            tmp[i] += (fishbowl[i + 1] - fishbowl[i]) // 5
            tmp[i + 1] -= (fishbowl[i + 1] - fishbowl[i]) // 5
    # print(f"조절:{tmp}")
    for i in range(N):
        fishbowl[i] = fishbowl[i] + tmp[i]

def unfold():
    new_fish = []
    if leftcount == 0:  ##진행방향 서쪽 , 남쪽이 왼쪽
        for i in range(10, -1, -1):
            for j in range(10, -1, -1):
                if board[i][j] != -1:
                    new_fish.append(fishbowl[board[i][j]])
    if leftcount == 1: # 진행방향 남쪽 ,  동쪽이 왼쪽
        for j in range(10, -1, -1):
            for i in range(0, 10, 1):
                if board[i][j] != -1:
                    new_fish.append(fishbowl[board[i][j]])
    if leftcount == 2: #동 북
        for i in range(0, 10, 1):
            for j in range(0, 10, 1):
                if board[i][j] != -1:
                    new_fish.append(fishbowl[board[i][j]])
    if leftcount == 3: #북 서
        for j in range(0, 10, 1):
            for i in range(10, -1, -1):
                if board[i][j] != -1:
                    new_fish.append(fishbowl[board[i][j]])
    for i in range(len(indexing), N):
        new_fish.append((fishbowl[i]))
    return new_fish

def fold():
    new_fish = []
    halfboard = [[0] * N for _ in range(4)]
    for i in range(N):
        halfboard[0][i] = fishbowl[i]
    for i in range(N//2):
        halfboard[1][-1-i] = halfboard[0][i]
        halfboard[0][i] = 0
    for i in range(0,2):
        for j in range(N//2,N//2 + N//4):
            halfboard[-1-i][N//2-1-j] = halfboard[i][j]
            halfboard[i][j] = 0
    # print("-----------just fold--------")
    # for i in halfboard:
    #     print(i)


    tmp = [0] * N
    idx = 0
    ##좌우 물고기 양 비교
    for j in range(N//2+N//4,N-1):
        for i in range(4):
            if halfboard[i][j] - halfboard[i][j+1] >= 5:
                tmp[idx] -= (halfboard[i][j] - halfboard[i][j+1]) //5
                tmp[idx + 4] += (halfboard[i][j] - halfboard[i][j+1]) //5
            if halfboard[i][j+1] - halfboard[i][j] >= 5:
                tmp[idx] += (halfboard[i][j+1] - halfboard[i][j]) //5
                tmp[idx + 4] -= (halfboard[i][j+1] - halfboard[i][j]) //5
            idx += 1
    ##상하 물고기 비교
    idx = 0
    for j in range(N // 2 + N // 4, N):
        for i in range(3):
            if halfboard[i][j] - halfboard[i+1][j] >= 5:
                tmp[idx] -= (halfboard[i][j] - halfboard[i+1][j]) // 5
                tmp[idx + 1] += (halfboard[i][j] - halfboard[i+1][j]) // 5
            if halfboard[i+1][j] - halfboard[i][j] >= 5:
                tmp[idx] += (halfboard[i+1][j] - halfboard[i][j]) // 5
                tmp[idx + 1] -= (halfboard[i+1][j] - halfboard[i][j]) // 5
            idx += 1
        idx += 1
    # print(f"조절:{tmp}")

    for j in range(N//2+N//4,N):
        for i in range(4):
            new_fish.append(halfboard[i][j])
    for i in range(N):
        new_fish[i] = new_fish[i] + tmp[i]
    return new_fish

def check():
    flag = max(fishbowl) - min(fishbowl) <= K
    return flag

N, K = map(int, input().split())
fishbowl = list(map(int, input().split()))
board = [[-1] * 11 for _ in range(11)]
indexing = {}
dir = [[0,-1],[1,0],[0,1],[-1,0]] #서,남,동,북



leftcount = makeBoard()
# for i in board:
#     print(i)

ans = 0
while not check():
    # print(f"원본:{fishbowl}")
    plusone()
    # print(f"플일:{fishbowl}")
    stackup()
    # print(f"말조:{fishbowl}")
    fishbowl = unfold()
    # print(f"풀고:{fishbowl}")
    fishbowl = fold()
    # print(f"반접:{fishbowl}")
    # print(check())
    ans += 1
print(ans)






