from A.B import *
S(0, 'azder', 'sample_')

def dfs(idx,cnt,sum):
    if cnt == 2:
        global ans
        ans = max(sum,ans)

    if idx == n:
        return

    dfs(idx + 1,cnt,sum)
    dfs(idx +1, cnt +1, sum + solo_line_max[idx])

T = int(input())
for test_case in range(1, T + 1):
    n,m,c = map(int ,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    solo_line_max=[0]*n
    for i in range(n):
        for j in range(n):
            cnt = 0
            tmp = 0
            for k in range(m):
                if j+k>=n:
                    break
                if board[i][j+k] + tmp <=c:
                    cnt += board[i][j+k] * board[i][j+k]
                    tmp += board[i][j+k]
                else:
                    break
            solo_line_max[i] = max(cnt, solo_line_max[i])
    dfs(0,0,0)
    print(solo_line_max)

    # if n >= 2*m:
    #     for i in range(n):
    #         for j in range(n - m - m + 1):
    #             cnt = 0
    #             tmp = 0
    #             for k in range(m):
    #                 if board[i][j + k] + tmp <= c:
    #                     cnt += board[i][j + k] * board[i][j + k]
    #                     tmp += board[i][j + k]
    #                 else:
    #                     break
    #             for l in range(j+m,n):
    #                 cnt2 = 0
    #                 tmp2 = 0
    #                 for k in range(m):
    #                     if l + k >= n:
    #                         break
    #                     if board[i][j + k] + tmp2 <= c:
    #                         cnt2 += board[i][l + k] * board[i][l + k]
    #                         tmp2 += board[i][l + k]
    #                     else:
    #                         break
    #                 ans = max(ans, cnt+cnt2)



    print(f'#{test_case} {ans}')

E(0, 'azder', 'sample_')