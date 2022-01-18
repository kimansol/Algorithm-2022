# https://www.acmicpc.net/problem/2669
# 백준2669/ 직사각형 네개의 합집합의 면적 구하기
# 2022.01.18

squre = [list(map(int,input().split()))for _ in range(4)]
board = [[0] * 100 for _ in range(100)] ## squre의 x2,y2의 최댓값을 찾아 보드를 만들면 더 적은 메모리,시간이 들겠지만 100이니 그냥 함

for x1,y1,x2,y2 in squre:
    for i in range(x1,x2):
        for j in range(y1,y2):
            if board[i][j] == 0:
                board[i][j] = 1

ans = 0
for i in board:
    ans += sum(i)

print(ans)

