from A.B import *
S(2, 'azder', 's_')


def dfs(bat,cur,cnt):
    global answer
    if cur == lst[0]:
        answer = min(cnt, answer)
        return
    if cnt >= answer:
        return

    if lst[cur] > bat:
        dfs(lst[cur]-1,cur+1,cnt+1)
    if bat != 0:
        dfs(bat-1, cur +1, cnt)
    return

T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    answer = 10e999
    dfs(lst[1]-1,2,0)

    print(f'#{test_case} {answer}')

E(2, 'azder' ,'s_')