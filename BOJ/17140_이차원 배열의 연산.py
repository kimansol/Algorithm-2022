#https://www.acmicpc.net/problem/17140
# 이차원 배열의 연산/ 골드4
#22.02.17


def r_calculate():
    max_length = 0
    for i in range(len(board)):
        tmp = {}
        for num in board[i]:
            if num == 0:
                continue
            tmp[num] = board[i].count(num)
        tmp = sorted(tmp.items(), key=lambda x: (x[1],x[0]))
        board[i] = []
        # if len(tmp) > 50:
        #     for j in range(50):
        #         board[i].append(tmp[j][0])
        #         board[i].append(tmp[j][1])
        # else:
        for j in range(len(tmp)):
            board[i].append(tmp[j][0])
            board[i].append(tmp[j][1])
        max_length = max(max_length,len(board[i]))
    for i in range(len(board)):
        for j in range(max_length-len(board[i])):
            board[i].append(0)

r,c,k = map(int ,input().split())
board = [list(map(int, input().split())) for _ in range(3)]
ans = 0

while ans <= 100:
    if r-1 < len(board) and c-1 < len(board[0]):
        if board[r-1][c-1] == k:
            break
    if len(board) >= len(board[0]):
        r_calculate()
    elif len(board) < len(board[0]):
        board = list(map(list, zip(*board[::-1])))
        r_calculate()
        board = list(map(list, zip(*board)))
    ans +=1

print(ans if ans <= 100 else -1)
