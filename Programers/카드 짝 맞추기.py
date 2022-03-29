from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations


def go(r, c, num, board):
    tmp = 0
    if board[r][c] == num:
        return r, c, tmp

    visited = [[0] * 4 for _ in range(4)]
    visited[r][c] = 1

    q = deque()
    q.append([r, c, 0])
    while q:
        x, y, cnt = q.popleft()

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 한칸 이동
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                continue
            if visited[nx][ny] == 1:
                continue
            if board[nx][ny] == num:
                return nx, ny, cnt + 1
            visited[nx][ny] = 1
            q.append([nx, ny, cnt + 1])

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 뭔가 만날때까지 이동
            cx, cy, nx, ny = x, y, 0, 0
            while 1:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                    nx, ny = cx, cy
                    break
                if board[nx][ny] != 0:
                    break
                cx, cy = nx, ny
            if visited[nx][ny] == 1:
                continue
            if board[nx][ny] == num:
                return nx, ny, cnt + 1
            visited[nx][ny] = 1
            q.append([nx, ny, cnt + 1])


def find_fair(r, c, lst, board):
    nr, nc = -1, -1
    for fr, fc in lst:
        if fr != r or fc != c:
            nr, nc = fr, fc
            break
    tmp = 0

    visited = [[0] * 4 for _ in range(4)]
    dq = deque()
    dq.append([r, c, 0])
    while dq:
        x, y, cnt = dq.popleft()
        if x == nr and y == nc:
            tmp = cnt
            break

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 한칸 이동
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                continue
            if visited[nx][ny] == 1:
                continue
            visited[nx][ny] = 1
            dq.append([nx, ny, cnt + 1])

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 뭔가 만날때까지 이동
            cx, cy, nx, ny = x, y, 0, 0
            while 1:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                    nx, ny = cx, cy
                    break
                if board[nx][ny] != 0:
                    break
                cx, cy = nx, ny
            if visited[nx][ny] == 1:
                continue
            visited[nx][ny] = 1
            dq.append([nx, ny, cnt + 1])
    return nr, nc, tmp


def solution(board, r, c):
    answer = 10e999
    fair_dict = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                fair_dict[board[i][j]].append([i, j])

    print(fair_dict)
    for case in permutations(fair_dict.keys()):

        cr, cc = r, c
        nboard = deepcopy(board)
        tmp = 0
        # print(case,s)
        for num in case:
            cr, cc, cnt = go(cr, cc, num, nboard)
            tmp += cnt + 1
            if tmp >= answer:
                break
            nboard[cr][cc] = 0

            cr, cc, cnt = find_fair(cr, cc, fair_dict[num], nboard)
            tmp += cnt + 1
            if tmp >= answer:
                break
            nboard[cr][cc] = 0
        else:
            answer = min(answer, tmp)
    return answer


# from collections import deque, defaultdict
# from copy import deepcopy
# from itertools import permutations
#
#
# def go(r, c, lst, board):
#     tmp = 0
#     if r == lst[0] and c == lst[1]:
#         return r, c, tmp
#
#     visited = [[0] * 4 for _ in range(4)]
#     visited[r][c] = 1
#
#     q = deque()
#     q.append([r, c, 0])
#     while q:
#         x, y, cnt = q.popleft()
#
#         for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 한칸 이동
#             nx, ny = x + dx, y + dy
#             if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
#                 continue
#             if visited[nx][ny] == 1:
#                 continue
#             if nx == lst[0] and ny == lst[1]:
#                 return nx, ny, cnt + 1
#             visited[nx][ny] = 1
#             q.append([nx, ny, cnt + 1])
#
#         for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 뭔가 만날때까지 이동
#             cx, cy, nx, ny = x, y, 0, 0
#             while 1:
#                 nx, ny = cx + dx, cy + dy
#                 if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
#                     nx, ny = cx, cy
#                     break
#                 if board[nx][ny] != 0:
#                     break
#                 cx, cy = nx, ny
#             if visited[nx][ny] == 1:
#                 continue
#             if nx == lst[0] and ny == lst[1]:
#                 return nx, ny, cnt + 1
#             visited[nx][ny] = 1
#             q.append([nx, ny, cnt + 1])
#
#
# def find_fair(r, c, lst, board):
#     nr, nc = -1, -1
#     for fr, fc in lst:
#         if fr != r or fc != c:
#             nr, nc = fr, fc
#             break
#     tmp = 0
#
#     visited = [[0] * 4 for _ in range(4)]
#     dq = deque()
#     dq.append([r, c, 0])
#     while dq:
#         x, y, cnt = dq.popleft()
#         if x == nr and y == nc:
#             tmp = cnt
#             break
#
#         for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 한칸 이동
#             nx, ny = x + dx, y + dy
#             if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
#                 continue
#             if visited[nx][ny] == 1:
#                 continue
#             visited[nx][ny] = 1
#             dq.append([nx, ny, cnt + 1])
#
#         for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 뭔가 만날때까지 이동
#             cx, cy, nx, ny = x, y, 0, 0
#             while 1:
#                 nx, ny = cx + dx, cy + dy
#                 if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
#                     nx, ny = cx, cy
#                     break
#                 if board[nx][ny] != 0:
#                     break
#                 cx, cy = nx, ny
#             if visited[nx][ny] == 1:
#                 continue
#             visited[nx][ny] = 1
#             dq.append([nx, ny, cnt + 1])
#
#     return nr, nc, tmp
#
#
# def solution(board, r, c):
#     answer = 10e999
#     fair_dict = defaultdict(list)
#     for i in range(4):
#         for j in range(4):
#             if board[i][j] != 0:
#                 fair_dict[board[i][j]].append([i, j])
#
#     for case in permutations(fair_dict.keys()):
#         # print(case)
#         for s in range(2**len(case)):
#             s = bin(s)[2:]
#             if len(s) < len(case):
#                 s = '0' * (len(case)-len(s)) + s
#             s=list(map(int,s))
#
#             cr, cc = r, c
#             nboard = deepcopy(board)
#             tmp = 0
#             # print(case,s)
#             for i in range(len(case)):
#                 cr, cc, cnt = go(cr, cc, fair_dict[case[i]][s[i]], nboard)
#                 tmp += cnt + 1
#                 if tmp >= answer:
#                     break
#                 nboard[cr][cc] = 0
#
#                 cr, cc, cnt = find_fair(cr, cc, fair_dict[case[i]], nboard)
#                 tmp += cnt + 1
#                 if tmp >= answer:
#                     break
#                 nboard[cr][cc] = 0