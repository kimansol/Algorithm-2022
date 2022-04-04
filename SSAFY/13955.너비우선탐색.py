from A.B import *
S(19, 'azder', 's_')

def bfs(s,n):
    q = []
    visited = [0] * n

    q.append(s)
    visited[s] = 1
    ans.append(s)

    while q:
        s = q.pop(0)
        for e in range(1, n):
            if visited[e] == 0 and adj[s][e] == 1:
                q.append(e)
                visited[e] = 1
                ans.append(e)


T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    adj = [[0] * (v+1) for _ in range(v+1)]
    ans = []
    for _ in range(e):
        a, b = map(int, input().split())
        adj[a][b] = 1
        adj[b][a] = 1
    bfs(1, v+1)
    print(f'#{test_case}', *ans)

E(19, 'azder', 's_')