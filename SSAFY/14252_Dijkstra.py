from A.B import *
S(2, 'azder')

def dijkstra(s, V):
    U = [0] * (V)  # 비용이 결정된 정점을 표시
    U[s] = 1  # 출발점 비용 결정
    for i in range(V):
        D[i] = adjM[s][i]

    # 남은 정점의 비용 결정
    for _ in range(V):  # 남은 정점 개수만큼 반복
        # D[w]가 최소인 w 결정, 비용이 결정되지 않은 정점w 중에서
        minV = 10e999
        w = 0
        for i in range(V):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1  # 비용 결정
        for v in range(V):
            if 0 < adjM[w][v] < 10e999:
                D[v] = min(D[v], D[w] + adjM[w][v])

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adjM = [[10e999] * V for _ in range(V)]
    for i in range(V):
        adjM[i][i] = 0
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w

    D = [0] * (V)
    dijkstra(0, V)
    print(f'#{test_case} {D[-1]}')

E(2, 'azder')