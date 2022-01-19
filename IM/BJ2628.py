## https://www.acmicpc.net/problem/2628
# 백준 2628/ 종이자르기

R,C = map(int,input().split())
n = int(input())
cut = [list(map(int,input().split(' '))) for i in range(n)] #0가로컷 1세로컷

x = [0] * R
y = [0] * C

for d, pos in cut:
    if d == 0:
        for i in range(pos):
            y[i] += 1
    else:
        for i in range(pos):
            x[i] += 1
xmax = 1
xcnt = 1
xflg = x[0]
for i in range(1,R):
    if x[i] == x[i-1]:
        xcnt+=1
        xmax = max(xcnt, xmax)
    else:
        xflg = x[i]
        xmax = max(xcnt, xmax)
        xcnt = 1

ymax = 1
ycnt = 1
yflg = y[0]
for i in range(1,C):
    if y[i] == y[i-1]:
        ycnt+=1
        ymax = max(ycnt, ymax)
    else:
        yflg=y[i]
        ymax = max(ycnt, ymax)
        ycnt=1

print(xmax * ymax)


'''
10 8
3
0 3
1 4
0 2
'''