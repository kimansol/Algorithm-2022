# https://www.acmicpc.net/problem/19236
# 백준19236 / 청소년 상어(삼성 기출) / 구현, 시뮬, 백트래킹
# 2022.01.16

from copy import deepcopy

# 해당번호의 물고기의 위치 찾기
def find_fish(arr, n):
    for x in range(4):
        for y in range(4):
            if arr[x][y][0] == n:
                return (x, y)
    return False

# 물고기 움직이기
def move_all_fish(arr, now_x, now_y):
    for i in range(1, 17):
        # 물고기의 좌표를 찾아옴
        postion = find_fish(arr, i)
        if not postion:
            continue
        x, y = postion
        d = arr[x][y][1]
        # 최대 8번 변환
        for _ in range(8):
            # 해당 방향으로 움직임
            nx,ny = x + dir[d][0], y + dir[d][1]
            # 벽이거나 상어의 위치라면 방향을 돌리고 다음탐색
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or (nx == now_x and ny == now_y):
                d = (d+1) % 8
                continue
            # 가능하다면 두 위치를 바꿈
            arr[x][y][1] = d
            arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
            break

# 이동 가능한 영역 찾기
def get_possible_positions(arr, now_x, now_y):
    smlist = []
    d = arr[now_x][now_y][1]
    for _ in range(3):
        now_x,now_y = now_x + dir[d][0], now_y + dir[d][1]
        # 벽이거나 빈공간이라면 다음탐색
        if now_x < 0 or now_y < 0 or now_x >= 4 or now_y >= 4 or arr[now_x][now_y][0] == 0:
            continue
        # 가능하다면 이동목록에 추가
        smlist.append((now_x, now_y))
    return smlist


def dfs(array, now_x, now_y, total):
    global result
    array = deepcopy(array)
    # 물고기 번호 더하기
    total += array[now_x][now_y][0]
    # 물고기 먹음 처리
    array[now_x][now_y][0] = 0
    # 물고기 이동
    move_all_fish(array, now_x, now_y)
    # 이동가능한 영역 찾기
    smlist = get_possible_positions(array, now_x, now_y)

    # 이동가능한 영역이 없다면 결과값을 비교하여 바꿈
    if len(smlist) == 0:
        result = max(result, total)
        return

    # 이동 가능하다면 다음 좌표들에 대해 탐색 시행
    for next_x, next_y in smlist:
        dfs(array, next_x, next_y, total)

# 상 좌상 좌 좌하 하 우하 우 우상
dir = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
board = [[0] * 4 for _ in range(4)]


data = [list(map(int, input().split())) for _ in range(4)]
for i in range(4):
    for j in range(4):
        board[i][j] = [data[i][j*2], data[i][j*2+1]-1]

result = 0
dfs(board, 0, 0, result)
print(result)

