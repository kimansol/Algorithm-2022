#농작물 수확하기
#22.02.06

from A.B import *
S(15, 'azder')
T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n= int(input())
    board = [list(map(int, input())) for _ in range(n)]
    ans = 0
    idx = n//2
    for i in range(n//2):
        ans += sum(board[i][idx:n-idx])
        idx -= 1
    ans += sum(board[n//2])
    idx = 1
    for i in range(n//2+1, n):
        ans += sum(board[i][idx:n-idx])
        idx += 1

    print(f'#{test_case} {ans}')

E(15, 'azder')

# from A.B import *
# from collections import deque

# S(15, 'azder')

# T = int(input())
#     # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     n= int(input())
#     board = [list(map(int, input())) for _ in range(n) ]
    
#     ans = 0
#     q = deque()
#     q.append((n//2,n//2, 0))
#     ans += board[n//2][n//2]
#     board[n//2][n//2] = -1
#     while q:
#         x,y,d = q.popleft()
#         for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
#             nx, ny = x + dx, y + dy
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             elif board[nx][ny] == -1:
#                 continue
#             elif d == n//2:
#                 continue
#             q.append((nx,ny,d+1))
#             ans += board[nx][ny]
#             board[nx][ny] = -1
#     print(f'#{test_case} {ans}')
 
# E(15, 'azder')