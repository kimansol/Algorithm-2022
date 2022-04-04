from A.B import *
from collections import defaultdict, deque
S(22, 'azder', 's_')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    v,e = map(int, input().split())
    edges = defaultdict(list)
    for _ in range(e):
        ns,ne = map(int, input().split())
        edges[ns].append(ne)
        edges[ne].append(ns)
    start, end = map(int, input().split())
    answer = 0

    q= deque([[start, 0]])
    visted = [0] * (v+1)
    visted[start] = 1

    while q:
        node, dis = q.popleft()
        if node == end:
            answer = dis
            break

        for next_node in edges[node]:
            if visted[next_node]:
                continue
            q.append([next_node,dis+1])
            visted[next_node] = 1
    print(f'#{test_case} {answer}')

E(22, 'azder', 's_')