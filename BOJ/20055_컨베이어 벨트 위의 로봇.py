# https://www.acmicpc.net/problem/20055
# 컨베이어 벨트 위으 로봇/ 골드5
# 2022.02.17

from collections import deque

n, k = map(int,input().split())
belt = list(map(int, input().split()))
q = deque()

def rota():
    tmp = belt[-1]
    for i in range(1,len(belt)):
        belt[i] = belt[i-1]
    belt[0] = tmp

def move():
    for i in range(len(q)):
        n = q.popleft()
        n = n + 1
        if n == 2*n-1:
            continue
        nn = 0 if n >11 else n+1

def up():
    if belt[0] != 0:
        q.append(0)

while belt.count(0) < k:
    rota()
    move()
    up()