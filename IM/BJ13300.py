# https://www.acmicpc.net/problem/13300
# 백준13300/방배정/브론즈2
# 2022.01.21

n , k = map(int, input().split())
student = [[0,0] for _ in range(6)]

for i in range(n):
    sex,age = map(int, input().split())
    student[age-1][sex] += 1

ans = 0
for f,m in student:
    ans += f // k
    ans += m // k
    ans += 1 if f % k != 0 else 0
    ans += 1 if m % k != 0 else 0

print(ans)
