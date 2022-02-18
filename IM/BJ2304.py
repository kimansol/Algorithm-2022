# https://www.acmicpc.net/problem/2304
# 백준 2304/ 창고 다각형
# 2022.01.19

n = int(input())
barList = [list(map(int,input().split(' '))) for _ in range(n)]
barList.sort()
max_val = 0
max_idx = []
for i in range(n):
    if barList[i][1] > max_val:
        max_val = barList[i][1]
        max_idx = [i]
    elif barList[i][1] == max_val:
        max_idx.append(i)

# print(barList)
# print(max_val,max_idx)
for i in range(max_idx[0],max_idx[-1]):
    barList[i][1] = max_val

for i in range(1,max_idx[0]):
    if barList[i][1] < barList[i-1][1]:
        barList[i][1] = barList[i-1][1]

for i in range(n-2,max_idx[-1],-1):
    if barList[i][1] < barList[i+1][1]:
        barList[i][1] = barList[i+1][1]
# print(barList)

ans = (barList[max_idx[-1]][0]-barList[max_idx[0]][0]+1) * max_val
# print(ans)
for i in range(max_idx[0]):
    ans += (barList[i+1][0] - barList[i][0]) * barList[i][1]
# print(ans)
for i in range(n-1,max_idx[-1],-1):
    ans += (barList[i][0] - barList[i-1][0]) * barList[i][1]
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
