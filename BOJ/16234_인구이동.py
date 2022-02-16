#https://www.acmicpc.net/problem/16234
# 인구이동/ 골드5
#2022.02.16 ##1:30 ##2:08
from collections import deque

n,l,r = map(int, input().split())
board =[list(map(int,input().split())) for _ in range(n)]
q = deque()

group = []
ans = 0
while 1:
    group = []
    visit = [[-1] * n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == -1:
                group_sum = board[i][j]
                group_cnt = 1
                visit[i][j] = idx
                q.append((i,j))
                while q:
                    x,y = q.popleft()
                    for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                        nx,ny = x + dx, y + dy
                        if nx <0 or ny <0 or nx>=n or ny >=n:
                            continue
                        if visit[nx][ny] == -1 and l <= abs(board[x][y]-board[nx][ny]) <= r:
                            visit[nx][ny] = idx
                            group_sum += board[nx][ny]
                            group_cnt += 1
                            q.append((nx,ny))
                group.append([group_sum,group_cnt])
                idx += 1
    if len(group) == n*n:
        break
    for i in range(n):
        for j in range(n):
            board[i][j] = group[visit[i][j]][0]//group[visit[i][j]][1]
    ans+=1
print(ans)