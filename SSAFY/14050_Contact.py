from A.B import *
S(10, 'azder')
from collections import defaultdict, deque

for test_case in range(1, 11):
    n, start = map(int, input().split())
    lst = list(map(int, input().split()))
    edges = defaultdict(list)
    for i in range(0,n,2):
        edges[lst[i]].append(lst[i+1])
    distance = [-1] * 101
    distance[start] = 0
    q = deque([start])
    max_distance = 0

    while q:
        cur_node = q.popleft()
        for nxt_node in edges[cur_node]:
            if distance[nxt_node] == -1:
                distance[nxt_node] = distance[cur_node] + 1
                max_distance = distance[nxt_node]
                q.append(nxt_node)

    answer = 0
    for i in range(1,101):
        if distance[i] == max_distance:
            answer = i

    print(f'#{test_case} {answer}')


E(10, 'azder')