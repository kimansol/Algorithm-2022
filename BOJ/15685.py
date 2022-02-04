#https://www.acmicpc.net/problem/15685
#백준 15685/ 드래곤커브 / 골드4
#2022.01.26

board = [[0] * 101 for _ in range(101)]
dir = [[0, 1], [-1, 0], [0, -1], [1, 0]] # 동 북 서 남

def make(move_list,g):
    if g == 0:
        return move_list
    for i in range(len(move_list)-1,-1, -1):
        move_list.append((move_list[i]+1)%4)
    return make(move_list, g-1)

n = int(input())
for i in range(n):
    y, x, d, g = map(int, input().split(' '))
    move_list = [d]
    board[x][y] = 1
    for d in make(move_list, g):
        nx, ny = x + dir[d][0], y + dir[d][1]
        board[nx][ny] = 1
        x,y = nx, ny

ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i][j+1] == 1 and board[i+1][j] == 1 and board[i+1][j+1] == 1:
            ans += 1

print(ans)
