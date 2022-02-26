#https://www.acmicpc.net/problem/2110
#공유기 설치/ 골드5
# 2022.02.19

def set_wifi(mid):
    cnt = 1
    cur_pos = house[0]
    for i in range(1,n):
        if house[i] - cur_pos < mid:
            continue
        else:
            cur_pos = house[i]
            cnt += 1
    return cnt


n, c = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))
house.sort()
ans = 0
left = 1
right = house[-1]-house[0]

while left <= right:
    mid = (left + right) // 2
    cnt = set_wifi(mid)
    if cnt >= c:
        left = mid +1
        if cnt == c:
            ans = max(ans,mid)
    else:
        right = mid-1

print(ans)