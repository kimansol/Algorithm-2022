# https://www.acmicpc.net/problem/2304
# 백준 2304/ 창고 다각형
# 2022.01.19

n = int(input())
barList = [list(map(int,input().split(' '))) for _ in range(n)]
barList.sort()
max = max(barList[i][1] for i in range(n))

for i in range(n-1):
    if barList[i][1] == max:
        for j in range(i,n-1):
            if barList[j][1] == max:
                for k in range(i,j+1):
                    barList[k][1] = max
        break
    if barList[i][1] >= barList[i+1][1]:
        barList[i+1][1] = barList[i][1]
for i in range(-1,-n,-1):
    if barList[i][1] == max:
        for j in range(i, -n,-1):
            if barList[j][1] == max:
                for k in range(i, j + 1):
                    barList[k][1] = max
        break
    if barList[i][1] >= barList[i-1][1]:
        barList[i-1][1] = barList[i][1]

ans = 0
for i in range(n-1):
    if barList[i][1] < barList[i+1][1]:
        ans += (barList[i+1][0] - barList[i][0]) * barList[i][1]
    if barList[i][1] == barList[i+1][1]:
        ans += (barList[i+1][0] - barList[i][0]) * barList[i][1]
    if barList[i][1] > barList[i+1][1]:
        ans += barList[i][1]
        ans += (barList[i+1][0] - barList[i][0] -1) * barList[i+1][1]
ans += barList[-1][1]

print(ans)






'''
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6
'''
