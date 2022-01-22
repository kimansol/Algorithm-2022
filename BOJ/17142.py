# https://www.acmicpc.net/problem/17142
# 백준 17142/ 연구소3(삼성 기출)
# 2022.01.22


def bfs():
    pass

def seletVirus(cnt, flag):
    if cnt == m:
        bfs(flag)
        return


n, m = map(int, input().split())
board = [list(map(int,input().split(' '))) for _ in range(n)]
virus = []

wallcnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            wallcnt += 1
        if board[i][j] == 2:
            virus.append([i,j])
viruscnt = len(virus)
blankcnt = n * n - wallcnt - viruscnt
virusflag = [False * viruscnt]

seletVirus(0, virusflag)




