n, k = map(int, input().split())
temps = list(map(int, input().split()))


# # n(1~100000)이 너무 커서 시간초과
# for i in range(0,n-k):
#     cnt = 0
#     for j in range(i,i+k):
#         cnt += temps[j]
#     ans = max(ans,cnt)
ret = 0
ans = 0
for i in range(k):
    ans += temps[i]

for i in range(1,n-k):
    cnt = ans
    print(cnt)
    ret = max(ans,cnt)

print(ret)