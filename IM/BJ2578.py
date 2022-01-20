# https://www.acmicpc.net/problem/2578
# 백준2578/ 빙고
#2022.01.20

board = [list(map(int, input().split(' '))) for _ in range(5)]
numbers = [list(map(int, input().split(' '))) for _ in range(5)]

def check():
    cnt = 0
    for i in range(5):
        if sum(board[i]) == 0:
            cnt += 1
    for i in range(5):
        tmp = 0
        for j in range(5):
            tmp += board[j][i]
        if tmp == 0:
            cnt += 1
    if board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4] == 0:
        cnt += 1
    if board[0][4] + board[1][3] + board[2][2] + board[3][1] + board[4][0] == 0:
        cnt += 1
    return cnt

def play():
    ans = 0
    for number in numbers:
        for num in number:
            for i in range(5):
                for j in range(5):
                    if board[i][j] == num:
                        board[i][j] = 0
                        break
            ans += 1
            if ans >= 12:
                if check() >= 3: ##동시에 2줄 이상이 같이 빙고가 되면서 4,5줄 이상이 한번에 될 수 있음
                    return ans
    return(-1)


print(play())


'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''