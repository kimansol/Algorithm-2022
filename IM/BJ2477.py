# https://www.acmicpc.net/problem/2477
# 백준2477 // 참외밭
# 2022.01.20

n = int(input())
moveList = [list(map(int,input().split( ))) for _ in range(6)]

## 가장 긴변을 찾음
xmax = 0
ymax = 0
for d,distance in moveList:
    if d in [1,2]:
        xmax = max(xmax,distance)
    if d in [3,4]:
        ymax = max(ymax,distance)


##회전을 하면서 가장 긴 두변을 지난 위치를 찾음
maxcnt = 0
mini_distance = []
flag = 0
for d,distance in moveList + moveList:
    if distance in [xmax,ymax] and flag == 0:
        maxcnt += 1
    else:
        maxcnt = 0
    if maxcnt == 2:
        flag = 1
    if flag == 1:
        mini_distance.append(distance)

print(((xmax * ymax - mini_distance[2] * mini_distance[3]) * n))

'''      
7
4 50
2 160
3 30
1 60
3 20
1 100
'''


