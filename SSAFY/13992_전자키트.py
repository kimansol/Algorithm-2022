from A.B import *
S(0, 'azder', 's_')

def dfs(cur_loc, cnt, visited,board):
    global answer
    if all(visited):
        cnt += board[cur_loc][0]
        answer = min(answer, cnt)
        return
    if cnt >= answer:
        return

    for i in range(1,n):
        if visited[i] == 0:
            visited[i] += 1
            dfs(i,cnt + board[cur_loc][i], visited, board)
            visited[i] -= 1

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = 10e999

    dfs(0,0,[1] + [0] * (n-1),board)
    print(f'#{test_case} {answer}')

E(0, 'azder', 's_')