# https://www.acmicpc.net/problem/20055
# 컨베이어 벨트 위으 로봇/ 골드5
# 2022.02.17

from collections import deque

n, k = map(int,input().split())
belt = list(map(int, input().split()))
q = deque()
belt = deque(belt)

def rota():
    belt.appendleft(belt.pop())
    for _ in range(len(q)):
        r_pos = q.popleft()
        r_pos += 1
        if r_pos < n-1:
            q.append(r_pos)

def move():
    for _ in range(len(q)):
        r_pos = q.popleft()
        nr_pos = r_pos+1
        if belt[nr_pos] > 0:
            if nr_pos == n-1:
                belt[nr_pos]-=1
            elif nr_pos in q:
                q.append(r_pos)
            elif nr_pos < n-1:
                q.append(nr_pos)
                belt[nr_pos] -= 1
        else:
            q.append(r_pos)


def up():
    if belt[0] != 0:
        q.append(0)
        belt[0] -= 1

ans = 0
while belt.count(0) < k:
    ans += 1
    rota()
    # print('---회전후----')
    # print(q)
    # print(belt)
    move()
    # print('---로봇이동후----')
    # print(q)
    # print(belt)
    up()
    # print('---새로봇추가후----')
    # print(q)
    # print(belt)

print(ans)
