# https://www.acmicpc.net/problem/2635
# 백준 2653/수이어가기
# 2022.01.18

#3만번 반복

n = int(input())

ans = 0
maxn = 0
for i in range(0,n+1):
    a = n
    b = i
    cnt = 2
    while 1:
        a, b = b, a - b
        if b < 0:
            break
        cnt += 1
    ans = max(cnt, ans)
    if ans == cnt:
        maxn = i

print(ans)
list = [n,maxn]
for i in range(2,ans):
    list.append(list[i-2] - list[i-1])
for i in list:
    print(i,end=' ')
