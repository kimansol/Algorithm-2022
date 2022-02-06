#행렬 찾기
#22.02.06

from A.B import *
S(10, 'azder')

def check_size(i,j):
    x,y = 0,0
    for k in range(i,n):
        if board[k][j] != 0:
            x += 1
        elif board[k][j] == 0:
            break 
    for l in range(j,n):
        if board[i][l] != 0:
            y += 1
        elif board[i][l] == 0:
            break
    return x, y 

def remove(i,j,x,y):
    for k in range(i,i+x):
        for l in range(j,j+y):
            board[k][l] = 0


T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n) ]
    ans =[]
    x,y = 0,0
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                x,y = check_size(i,j)
                remove(i,j,x,y)
                ans.append([x*y, x,y])
    ans.sort()
    print(f'#{test_case} {len(ans)} ',end='')
    for xy,x,y in ans:
        print(f'{x} {y}',end=' ')
    print()


E(10, 'azder')