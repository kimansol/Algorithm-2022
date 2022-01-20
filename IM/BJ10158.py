# https://www.acmicpc.net/problem/10158
# 백준 10158/ 개미 / 실버4
# 2022.01.20

w, h = map(int, input().split(' ')) ##맵크기
p, q = map(int, input().split(' ')) ##위치
t = int(input()) ## 시간

x, y = h - q, p

# t= 최대 2억 시간초과  이거 다 뻘짓
# dir =  [[-1,-1],[-1,1],[1,1],[1,-1]] #좌상,우상,우하,좌하
# d = 1
# for i in range(t):
#     nx, ny = x + dir[d][0], y + dir[d][1]
#     if (nx < 0 and ny <0) or (nx < 0 and ny >= w+1) or (nx >= h+1 and ny >=w+1) or (nx >= h+1 and ny<0):
#         d = (d+2) % 4
#     if nx < 0:
#         if d == 0: d = 3
#         if d == 1: d = 2
#     if ny < 0:
#         if d == 0: d = 1
#         if d == 3: d = 2
#     if nx >= h+1:
#         if d == 3: d = 0
#         if d == 2: d = 1
#     if ny >= w+1:
#         if d == 1: d = 0
#         if d == 2: d = 3
#     nx, ny = x + dir[d][0], y + dir[d][1]
#     x,y = nx, ny

a = t % (2 * h)
b = t % (2 * w)
idx = -1
for i in range(a):
    if x == 0 or x == h:
        idx = -idx
    x += idx

idx = 1
for i in range(b):
    if y == 0 or y == w:
        idx = -idx
    y += idx


print(y, h-x)
