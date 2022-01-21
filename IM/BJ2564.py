# https://www.acmicpc.net/problem/2564
# 백준 2564/ 경비원 / 실버1
# 2022.01.21

def position(x,y):
    if x == 1:
        x, y = 0, y
    elif x == 2:
        x, y = c, y
    elif x == 3:
        x, y = y, 0
    elif x == 4:
        x, y = y, r
    return x,y

r, c = map(int, input().split())
n = int(input())
stores = [list(map(int,input().split())) for _ in range(n)]  ##1 2 3 4 북 남 서 동
x,y = map(int, input().split())
dir = [[0,-1],[-1,0],[0,1],[1,0]] ## 서북동남

x,y = position(x, y)

for i in range(n):
    stores[i][0], stores[i][1] = position(stores[i][0], stores[i][1])

left = []
right = []

stores.sort()
for i in range(len(stores)-1):
    if stores[i][1] == stores[i+1][1] and stores[i][0] == stores[i+1][0]:
        n -= 1

if [x,y] in stores:
    n -= 1

if x == 0:
    d = 2
elif x== c:
    d = 0
elif y == 0:
    d = 1
else: d = 3
idx = 0
cx,cy = x, y
while len(left) < n:

    idx += 1
    nx, ny = cx + dir[d][0], cy + dir[d][1]
    if nx<0 or ny<0 or nx> c or ny > r:
        d = (d+1)%4
        nx, ny = cx + dir[d][0], cy + dir[d][1]
    cx, cy = nx, ny
    if [cx, cy] in stores:
        left.append(idx)

if x == 0:
    d = 0
elif x== c:
    d = 2
elif y == 0:
    d = 3
else: d = 1
idx = 0
cx,cy = x, y
while len(right) < n:
    idx += 1
    nx, ny = cx + dir[d][0], cy + dir[d][1]
    if nx<0 or ny<0 or nx> c or ny > r:
        d = (d+4-1)%4
        nx, ny = cx + dir[d][0], cy + dir[d][1]
    cx, cy = nx, ny
    if [cx, cy] in stores:
        right.append(idx)

# print(stores)
# print(x,y)
# print(left)
# print(right)

ans = 0
for i in range(n):
    ans += min(left[i],right[-i-1])
print(ans)

