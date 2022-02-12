#모노미노도미노
#https://www.acmicpc.net/problem/19235
#2022.02.11

n = int(input())

blocks = [list(map(int ,input().split())) for _ in range(n)]
# (t,x,y) 1(1,1), 2(1,2), 3(2,1)
blue = [[0] * 4 for _ in range(6)]
green= [[0] * 4 for _ in range(6)]

def down(t,x,y,board,idx):
    if t == 1:
        for i in range(6):
            if board[i][y] != 0:
                board[i-1][y] = idx
                break
            if i == 5:
                board[5][y] = idx
    elif t == 2:
        tmp = 0
        for i in range(6):
            if board[i][y] != 0:
                tmp = i-1
                break
            if i == 5:
                tmp = 5
        for i in range(6):
            if board[i][y+1] != 0:
                tmp = min(tmp, i-1)
                break
            if i == 5:
                tmp = min(tmp, 5)
        board[tmp][y] = idx
        board[tmp][y+1] = idx
    elif t == 3:
        for i in range(6):
            if board[i][y] != 0:
                board[i-1][y] = idx
                board[i-2][y] = idx
                break
            if i == 5:
                board[5][y] = idx
                board[4][y] = idx
    return board

def remove_line(board):
    global ans
    flag = 1
    while flag:
        flag = 0
        for k in range(5, 1, -1):
            if all(board[k]):
                flag = 1
                ans += 1
                if all(board[k-1]):
                    for i in range(k, 1, -1):
                        for j in range(4):
                            board[i][j] = board[i - 2][j]
                    ans += 1
                else:
                    for i in range(k, 0, -1):
                        for j in range(4):
                            board[i][j] = board[i - 1][j]
                downtmp = [k,k,k,k]
                for l in range(4):
                    for i in range(k+1,6):
                        if board[i][l] == 0:
                            downtmp[l] = i
                        else:
                            break
                for i in range(k, 1, -1):
                    for j in range(4):
                        if board[i][j] == 0:
                            continue
                        if j <= 2 and board[i][j] == board[i][j + 1]:
                            tmp = min(downtmp[j], downtmp[j+1])
                            downtmp[j] = tmp-1
                            downtmp[j+1] = tmp
                        else:
                            board[i][j],board[downtmp[j]][j] = 0,board[i][j]
                            downtmp[j] -= 1
                break
    return board

def over_range(board):
    cnt = 0
    if sum(board[0]) != 0:
        cnt +=1
    if sum(board[1]) != 0:
        cnt +=1
    if cnt == 1:
        for i in range(5,1,-1):
            for j in range(4):
                board[i][j] = board[i-1][j]
        board[1] = [0,0,0,0]
    if cnt == 2:
        for i in range(5,1,-1):
            for j in range(4):
                board[i][j] = board[i-2][j]
        board[0] = [0,0,0,0]
        board[1] = [0, 0, 0, 0]
    return board

ans = 0
for idx,(t,x,y) in enumerate(blocks):
    green = down(t, x, y,green, idx+1)
    if t == 2:
        t = 3
    elif t == 3:
        t = 2
    blue = down(t, y, x, blue, idx+1)
    green = remove_line(green)
    blue = remove_line(blue)
    green = over_range(green)
    blue = over_range(blue)


    sum_val = 0
    for i in range(2, 6):
        for j in range(4):
            if green[i][j] != 0:
                sum_val += 1
            if blue[i][j] != 0:
                sum_val += 1
    print(ans)
    print(sum_val)
    blue = list(map(list, zip(*blue[::-1])))
    for i in range(4):
        blue[i] = blue[i][::-1]
    for i in range(4):
        print(f'{green[i]}       {blue[i]}')
    for i in range(4,6):
        print(f'{green[i]}')
    for i in range(4):
        blue[i] = blue[i][::-1]
    blue = list(map(list, zip(*blue)))[::-1]
    #
    # # for i in range(6):
    # #     print(f'{green[i]}     {blue[i]}')


sum_val = 0
for i in range(2, 6):
    for j in range(4):
        if green[i][j] != 0:
            sum_val += 1
        if blue[i][j] != 0:
            sum_val += 1
print(ans)
print(sum_val)



