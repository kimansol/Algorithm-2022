##https://www.acmicpc.net/problem/14499
# 주사위 굴리기/ 골드4
# 2022.02.17

def move(x,y,d):
    nx,ny = x + dir[d][0], y + dir[d][1]
    if nx<0 or ny<0 or nx>=n or ny >=m:
        return x,y,dice
    if d == 1: #동
        new_dice = [dice[0],dice[4],dice[2],dice[5],dice[3],dice[1]]
    elif d == 2: #서
        new_dice = [dice[0], dice[5], dice[2], dice[4], dice[1], dice[3]]
    elif d == 3: #북
        new_dice = [dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]]
    else:
        new_dice = [dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]]

    if board[nx][ny] == 0:
        board[nx][ny] = new_dice[3]
    else:
        new_dice[3], board[nx][ny] = board[nx][ny], 0
    print(new_dice[1])
    return nx,ny,new_dice


n,m,x,y,k = map(int, input().split())
board = [list(map(int ,input().split())) for _ in range(n)]
order = []
if k >0:
    order = list(map(int, input().split()))

dir = [[0,0],[0,1],[0,-1],[-1,0],[1,0]] #0제자리 1동 2서 3북 4남
dice = [0,0,0,0,0,0]

for d in order:
    x,y,dice = move(x,y,d)