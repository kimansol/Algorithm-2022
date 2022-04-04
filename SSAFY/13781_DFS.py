from A.B import *
S(14, 'azder', 's_')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    adj = [[0]*(v+1) for _ in range(v+1)]
    stk = []
    visited = [0] * (v +1)
    for _ in range(e):
        v1,v2 = map(int, input().split())
        adj[v1][v2] = 1
        adj[v2][v1] = 1
    print(f'#{test_case} 1 ',end='')
    stk.append(1)
    visited[1] = 1

    while stk:
        for i in range(1,v+1):
            if adj[stk[-1]][i] == 1 and visited[i] == 1:
                continue
            elif adj[stk[-1]][i] == 1 and visited[i] == 0:
                stk.append(i)
                visited[i] = 1
                print(i,end=' ')
                break
        else:
            stk.pop()
    print()

E(14, 'azder', 's_')
