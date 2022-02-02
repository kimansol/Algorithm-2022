# https://www.acmicpc.net/problem/16235
# 백준16235/나무 재테크/ 골드4
# 2022.02.02

from collections import deque

def ss():
    for i in range(n):
        for j in range(n):
            for k in range(len(live_tree[i][j])):
                if live_tree[i][j][k] <= board[i][j]:
                    board[i][j] -= live_tree[i][j][k]
                    live_tree[i][j][k] += 1
                else:
                    for _ in range(k, len(live_tree[i][j])):
                        board[i][j] += live_tree[i][j].pop() // 2
                    break

def fw():
    for x in range(n):
        for y in range(n):
            for k in live_tree[x][y]:
                if k % 5 == 0:
                    for dx,dy in dir:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            live_tree[nx][ny].appendleft(1)
            board[x][y] += plus_board[x][y]


dir = [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 1], [1, 0], [0, -1], [0, 1]]
n, m, k = map(int, input().split())
plus_board = []
live_tree = [[deque() for i in range(n)] for i in range(n)]
board = [[5] * n for i in range(n)]
for i in range(n):
    plus_board.append(list(map(int, input().split())))
for i in range(m):
    x, y, z = map(int, input().split())
    live_tree[x - 1][y - 1].append(z)

for i in range(k):
    ss()
    fw()

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(live_tree[i][j])
print(cnt)

# from collections import deque
#
# def spring():
#     new_tree = deque()
#     for _ in range(len(live_tree)):
#         age, x, y = live_tree.popleft()
#         if age <= board[x][y]:
#             board[x][y] -= age
#             age += 1
#             live_tree.append((age, x, y))
#             if age % 5 == 0:
#                 for dx, dy in dir:
#                     nx, ny = x + dx, y + dy
#                     if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                         continue
#                     new_tree.append((1, nx, ny))
#         else:
#             dead_tree.append((age, x, y))
#     return new_tree + live_tree
#
# n, m, k = map(int, input().split())
# plus_board = [list(map(int, input().split())) for _ in range(n)]
# board = [[5] * n for _ in range(n)]
# dir = [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 1], [1, 0], [0, -1], [0, 1]]
#
# tree = []
# for _ in range(m):
#     x,y,age = map(int, input().split())
#     tree.append([age, x-1, y-1])
# tree.sort()
#
# live_tree = deque()
# for age, x, y in tree:
#     live_tree.append((age, x, y))
#
# dead_tree = deque()
#
# for _ in range(k):
#     live_tree = spring()
#
#     while dead_tree:
#         age, x, y = dead_tree.popleft()
#         board[x][y] += age // 2
#
#     for i in range(n):
#         for j in range(n):
#             board[i][j] += plus_board[i][j]
#
# print(len(live_tree))