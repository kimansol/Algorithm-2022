##백준 2259/수열
# https://www.acmicpc.net/problem/2559
# 2022.01.20


n, k = map(int, input().split())
temps = list(map(int, input().split()))


# # n(1~100000)이 너무 커서 시간초과
# for i in range(0,n-k):
#     cnt = 0
#     for j in range(i,i+k):
#         cnt += temps[j]
#     ans = max(ans,cnt)
ans = 0
for i in range(k):
    ans += temps[i]
ret = ans

for i in range(1,n-k+1): # 1 2 3 4 5
    ans -= temps[i-1]
    ans += temps[k+i-1] # 5 6 7 8 9
    ret = max(ans,ret)

print(ret)

