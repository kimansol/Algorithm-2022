# https://www.acmicpc.net/problem/17837
# 백준17837/ 새로운게임2/ 골드2
# 2022.01.23

def play():
    cnt = 0
    dir = [[0,1],[0,-1],[-1,0],[1,0]] ##동서북남
    while cnt <= 1000:
        cnt+=1
        for x,y,d,idx in mal:
            nx, ny = x + dir[d][0], y + dir[d][1]
            if nx <0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 2: #파 or 벽
                nd = d + 1 if d % 2 == 0 else d - 1
                nx, ny = x + dir[nd][0], y + dir[nd][1]
                if nx <0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 2: # 파 or 벽 *2
                    nx,ny,nd = x, y, nd
                    # for i in stackboard:
                    #     print(i)
                    # print(mal)
                    # input(idx)
                elif board[nx][ny] == 1: #파 or 벽 -> 빨
                    mal[idx] = [nx, ny, nd, idx]
                    for i in range(len(stackboard[x][y])):
                        if stackboard[x][y][i] == idx:
                            for j in stackboard[x][y][i:]:
                                mal[j][0], mal[j][1] = nx, ny
                            plus = stackboard[x][y][i:]
                            stackboard[nx][ny] += plus[::-1]
                            stackboard[x][y] = stackboard[x][y][0:i]
                            break
                    # for i in stackboard:
                    #     print(i)
                    # print(mal)
                    # input(idx)
                elif board[nx][ny] == 0: #파 or 벽 -> 흰
                    for i in range(len(stackboard[x][y])):
                        if stackboard[x][y][i] == idx:
                            for j in stackboard[x][y][i:]:
                                mal[j][0], mal[j][1] = nx, ny
                            stackboard[nx][ny] += stackboard[x][y][i:]
                            stackboard[x][y] = stackboard[x][y][0:i]
                            break
                    # for i in stackboard:
                    #     print(i)
                    # print(mal)
                    # input(idx)
                mal[idx] = [nx,ny,nd,idx]

            elif board[nx][ny] == 0: # 흰
                mal[idx] = [nx, ny, d, idx]
                for i in range(len(stackboard[x][y])):
                    if stackboard[x][y][i] == idx:
                        for j in stackboard[x][y][i:]:
                            mal[j][0],mal[j][1] = nx,ny
                        stackboard[nx][ny] += stackboard[x][y][i:]
                        stackboard[x][y] = stackboard[x][y][0:i]
                        break
                # for i in stackboard:
                #     print(i)
                # print(mal)
                # input(idx)

            elif board[nx][ny] == 1: #빨
                mal[idx] = [nx, ny, d, idx]
                for i in range(len(stackboard[x][y])):
                    if stackboard[x][y][i] == idx:
                        for j in stackboard[x][y][i:]:
                            mal[j][0], mal[j][1] = nx, ny
                        plus = stackboard[x][y][i:]
                        stackboard[nx][ny] += plus[::-1]
                        stackboard[x][y] = stackboard[x][y][0:i]
                        break
            for i in range(n):
                for j in range(n):
                    if len(stackboard[i][j]) >= 4:
                        #출력
                        for i in stackboard:
                            print(i)
                        print(mal)
                        return cnt
        # for i in stackboard:
        #     print(i)
        # print(mal)
        # input(f"{cnt} 번 이동")
    return -1

n, m = map(int, input().split(' ')) ## 보드크기, 말 갯수
board = [list(map(int,input().split())) for _ in range(n)]
stackboard = [[[] for _ in range(n)] for _ in range(n)]
# [[], [], [0, 1, 2, 3], []]
# [[], [], [], []]
# [[], [], [], []]
# [[], [], [], []]

mal = []
# [[0, 2, 1, 0], [0, 2, 1, 1], [0, 2, 1, 2], [0, 2, 2, 3]]
# [x, y, d, idx]

for i in range(m):
    x,y,d = map(int,input().split())
    mal.append([x-1,y-1,d-1,i])
    stackboard[x-1][y-1] = [i]

for i in stackboard:
    print(i)
print(mal)
print("초기상태")

print(play())