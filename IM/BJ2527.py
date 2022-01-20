# https://www.acmicpc.net/problem/2527
# 백준2527 / 직사각형 / 실버1
# 2022.01.20

quadrangles = [list(map(int, input().split(' '))) for _ in range(4)]

for x,y,p,q,x2,y2,p2,q2 in quadrangles:
    ans = ''
    if (x == p2 and q == y2) or (x == p2 and y == q2) or (p == x2 and q == y2) or (p == x2 and y == q2):
        ans = 'c'
    elif p < x2 or x > p2 or q < y2 or y > q2:
        ans = 'd'
    elif x == p2 or p == x2 or q == y2 or y == q2:
        ans = 'b'
    else:
        ans = 'a'
    print(ans)

'''
3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600
'''
