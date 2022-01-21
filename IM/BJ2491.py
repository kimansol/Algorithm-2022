# https://www.acmicpc.net/problem/2491
# 백준 2491/ 수열 / 실버3
# 2022.01.21

n =int(input())
num = list(map(int, input().split( )))

new = []
for i in range(n-1):
    new.append(num[i+1] - num[i])


plusidx = 1
minusidx = 1
ans = 1
for n in new:
    if n == 0:
        plusidx += 1
        minusidx += 1
        ans = max(ans, plusidx,minusidx)
    if n < 0:
        plusidx = 1
        minusidx +=1
        ans = max(ans, plusidx, minusidx)
    if n > 0:
        plusidx +=1
        minusidx = 1
        ans = max(ans, plusidx, minusidx)

print(ans)




