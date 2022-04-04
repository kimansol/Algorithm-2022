from A.B import *
S(18, 'azder', 's_')

def dfs(cur_node):
    global ans
    if ans == 1 or cur_node == 99:
        ans = 1
        return

    if path1[cur_node]:
        dfs(path1[cur_node])
    if path2[cur_node]:
        dfs(path2[cur_node])


T = 3
for test_case in range(1, T + 1):
    tt, n = map(int, input().split())
    numbers = list(map(int, input().split()))
    ans = 0
    path1= [0] * 100
    path2= [0] * 100
    for i in range(0,2*n,2):
        if path1[numbers[i]] != 0:
            path2[numbers[i]] = numbers[i+1]
        else:
            path1[numbers[i]] = numbers[i+1]

    dfs(0)

    print(f'#{test_case} {ans}')

E(18, 'azder', 's_')