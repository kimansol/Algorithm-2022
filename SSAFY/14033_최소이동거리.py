from A.B import *
S(3, 'azder', 's_')

def dfs(cur, des, cnt):
    global answer
    if cur == des:
        answer = min(answer, cnt)
        return

    if cnt >= answer:
        return

    if edges[cur]:
        for nxt,w in edges[cur]:
            dfs(nxt, des, cnt + w)

from collections import defaultdict
T = int(input())
for test_case in range(1, T+1):
    n,m = map(int, input().split())
    edges = defaultdict(list)
    for i in range(m):
        s,e,w = map(int,input().split())
        edges[s].append([e,w])
    answer = 10e999
    dfs(0,n,0)
    print(f'#{test_case} {answer}')


E(3, 'azder', 's_')