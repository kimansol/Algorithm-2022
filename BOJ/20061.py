##모노미노도미노2 골드2
#https://www.acmicpc.net/problem/20061
#2022.02.10

n = int(input())

blocks = [list(map(int ,input().split())) for _ in range(n)]
# (t,x,y) 1(1,1), 2(1,2), 3(2,1)
blue = [[0] * 4 for _ in range(6)]
green= [[0] * 4 for _ in range(6)]

def down(t,x,y,board):
    if t == 1:
        for i in range(6):
            if board[i][y] != 0:
                board[i-1][y] = 1
                break
            if i == 5:
                board[5][y] = 1
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
        board[tmp][y] = 1
        board[tmp][y+1] = 1
    elif t == 3:
        for i in range(6):
            if board[i][y] != 0:
                board[i-1][y] = 1
                board[i-2][y] = 1
                break
            if i == 5:
                board[5][y] = 1
                board[4][y] = 1
    return board

def remove_line(board):
    global ans
    flag = 0
    for k in range(5,1,-1):
        if sum(board[k]) == 4:
            if sum(board[k-1]) == 4: ##2줄 연속 일 경우 한번더 하기 위해
                flag = 1
            ans += 1
            for i in range(k,0,-1):
                for j in range(4):
                    board[i][j] = board[i - 1][j]
    if flag == 1:
        for k in range(5, 1, -1):
            if sum(board[k]) == 4:
                ans += 1
                for i in range(k, 0, -1):
                    for j in range(4):
                        board[i][j] = board[i - 1][j]
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
for t,x,y in blocks:
    green = down(t, x, y,green)
    if t == 2:
        t = 3
    elif t == 3:
        t = 2
    blue = down(t, y, x, blue)
    green = remove_line(green)
    blue = remove_line(blue)
    green = over_range(green)
    blue = over_range(blue)

print('---------------------')
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


sum_val = 0
for i in range(2,6):
    sum_val += sum(green[i])
    sum_val += sum(blue[i])
print(ans)
print(sum_val)
