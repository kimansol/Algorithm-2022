from A.B import *
S(6, 'azder', 's_')
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    ans = 0
    q = deque([[0,n]])
    visited = [0] * 1000001
    while q:
        cnt, num = q.popleft()
        if num == m:
            ans = cnt
            break

        if num <= 500000 and visited[num * 2] == 0:
            visited[num * 2] = 1
            q.append([cnt + 1, num * 2])
        if num <= 999999 and visited[num + 1] == 0:
            visited[num + 1] = 1
            q.append([cnt + 1, num + 1])
        if num - 1 > 0 and visited[ num - 1] == 0:
            visited[num - 1] = 1
            q.append([cnt + 1, num - 1])
        if num - 10 > 0 and visited[num - 10] == 0:
            visited[num - 10] = 1
            q.append([cnt + 1, num - 10])

    print(f'#{test_case} {ans}')

E(6, 'azder', 's_')