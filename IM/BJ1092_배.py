# https://www.acmicpc.net/problem/1092
# 배,1092 골드5
# 2022.02.18

n = int(input())
limit = list(map(int,input().split()))
limit.sort()
m = int(input())
box = list(map(int,input().split()))
box.sort()
ans = 0

if max(limit) < max(box):
    print(-1)
else:
    lift = [0] * n
    for i in range(m):
        for j in range(n):
            if box[i] <= limit[j]:
                lift[j] += 1
    while sum(lift) > 0:
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if lift[j] > 0:
                    lift[j] -= 1
                else:
                    break
            for j in range(i-1,-1,-1):
                if lift[j] > lift[i]:
                    lift[j] -= 1
                else:
                    break
        ans +=1
    print(ans)