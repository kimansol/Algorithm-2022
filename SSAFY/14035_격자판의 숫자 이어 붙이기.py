from A.B import *
S(5, 'azder', 'sample_')
# print(4**7 * 4  * 4) = 26만
def dfs(x,y,idx,numbers):
    if idx == 7:
        if numbers not in answer:
            answer.append(numbers)
        return

    for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
        nx,ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            continue
        dfs(nx,ny,idx+1,numbers+board[nx][ny])

T = int(input())
for test_case in range(1, T+1):
    board = [list(map(str, input().split())) for _ in range(4)]
    answer = []
    for i in range(4):
        for j in range(4):
            dfs(i,j,1,board[i][j])
    print(f'#{test_case}', len(answer))

E(5, 'azder', 'sample_')