from A.B import *

S(1, 'azder', 's_')

from collections import deque
T = int(input())
for test_case in range(1, T+1):
    n, m= map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int,input().split()))
    answer = 0
    w = deque(sorted(w,reverse=True))
    t = deque(sorted(t,reverse=True))
    cur_w,cur_t = 0, 0
    while w and t:
        if cur_w == 0:
            cur_w = w.popleft()
        if cur_t == 0:
            cur_t = t.popleft()
        if cur_t >= cur_w:
            answer += cur_w
            cur_w,cur_t = 0,0
        else:
            cur_w = 0

    print(f'#{test_case} {answer}')

E(1, 'azder', 's_')