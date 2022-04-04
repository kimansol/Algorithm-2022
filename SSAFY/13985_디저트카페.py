from A.B import *
S(8, 'azder', 'sample_')

def dfs(d,x,y,visited):
    global answer
    if d == 2 and answer>=len(visited)*2:
        return
    if d > 3:
        return
    if d == 3 and x == sx and y == sy and answer < len(visited):
        answer = len(visited)
        return

    for k in range(d,d+2):
        nx,ny = x + dir[d][0], y+ dir[d][1]
        if 0<=nx<n and 0<=ny<n and board[nx][ny] not in visited:
            visited.append(board[nx][ny])
            dfs(k,nx,ny,visited)
            visited.pop()


dir = [[1,-1],[1,1],[-1,1],[-1,-1],[0,0]]
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = -1
    for i in range(0,n-2):
        for j in range(1,n-1):
            sx,sy = i, j
            dfs(0,i,j,[])

    print(f'#{test_case} {answer}')


E(8, 'azder', 'sample_')