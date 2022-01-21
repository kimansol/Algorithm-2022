# https://www.acmicpc.net/problem/2605
# 백준2605 / 줄세우기/ 브론즈2
# 2022.01.21

n = int(input())
numbers = list(map(int,input().split(' ')))

line = [0 for _ in range(n)]

for i in range(n):
    line[i] = i+1
    for j in range(numbers[i]):
        line[i-j],line[i-j-1] = line[i-j-1],line[i-j]

for i in line:
    print(i,end=' ')


