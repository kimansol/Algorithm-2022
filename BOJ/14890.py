# https://www.acmicpc.net/problem/14890
# 백준14890/경사로/ 골드3
# 2022.02.03


n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def check(board):
    ret = 0
    for line in board:
        flag = True
        cnt = 0
        for i in range(len(line)):
            if i == 0:
                cnt += 1
            elif line[i] - line[i - 1] >= 2 or line[i - 1] - line[i] >= 2:
                flag = False
                break
            elif line[i] == line[i - 1]:
                cnt += 1
            elif line[i] - line[i - 1] == 1:
                if l <= cnt:
                    cnt = 1
                else:
                    flag = False
                    break
            elif line[i - 1] - line[i] == 1:
                if len(line) - i < l or cnt < 0:
                    flag = False
                    break
                cnt = -l + 1
            if i == len(line) - 1 and cnt < 0:
                flag = False
        if flag == True:
            ret += 1
    return ret

def rot(board):
    board = list(map(list, zip(*reversed(board))))
    return board

ans = 0
ans += check(board)
board = rot(board)
ans += check(board)

print(ans)

