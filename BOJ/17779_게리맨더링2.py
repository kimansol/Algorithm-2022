#https://www.acmicpc.net/problem/17779
#게리맨더링2/골드4/
#22.02.16 ##07:50

def group1(x,y,d1,d2):
    ret = 0
    for i in range(x):
        for j in range(y+1):
            ret += board[i][j]
    idx = 0
    for i in range(x,x+d1):
        for j in range(y-idx):
            ret += board[i][j]
        idx += 1
    return ret

def group2(x,y,d1,d2):
    ret = 0
    for i in range(x):
        for j in range(y+1,n):
            ret += board[i][j]
    idx = 0
    for i in range(x, x + d2 + 1):
        for j in range(y + 1 + idx, n):
            ret += board[i][j]
        idx += 1
    return ret

def group3(x,y,d1,d2):
    ret = 0
    idx = 0
    for i in range(x+d1,x+d1+d2+1):
        for j in range(y-d1 + idx):
            ret += board[i][j]
        idx += 1
    for i in range(x+d1+d2+1,n):
        for j in range(y-d1+d2):
            ret += board[i][j]
    return ret

def group4(x,y,d1,d2):
    ret = 0
    idx = 0
    for i in range(x + d2 + 1, x+d1+d2+1):
        for j in range(y + d2 - idx, n):
            ret += board[i][j]
        idx += 1
    for i in range(x + d1 + d2 + 1, n):
        for j in range(y-d1+d2,n):
            ret += board[i][j]
    return ret



ans = 10e999
n = int(input())
board = [list(map(int, input().split()))for _ in range(n)]
all_ingu = 0
for i in board:
    all_ingu += sum(i)
for i in range(1,n-2):
    for j in range(2,n-1):
        for k in range(1,j):
            if i+k+1>=n:
                continue
            for l in range(1,n-j):
                if i + k + l >= n:
                    continue
                ingu1= group1(i,j,k,l)
                ingu2= group2(i,j,k,l)
                ingu3= group3(i,j,k,l)
                ingu4= group4(i,j,k,l)
                ingu5= all_ingu - ingu1 -ingu3 - ingu2 -ingu4
                max_val = max(ingu5,ingu4,ingu3,ingu1,ingu2)
                min_val = min(ingu5,ingu4,ingu3,ingu1,ingu2)
                ans = min(ans,max_val-min_val)
print(ans)





