# https://www.acmicpc.net/problem/2309
# 백준 2309/ 일곱 난쟁이 / 브론즈 2
# 2022.01.21
a = []
for i in range(9):
    a.append(int(input()))
a.sort()

flag = [0,0,0,0,0,0,0,0,0]

def dfs(n,flag):
    if sum(flag) == 7:
        ans = 0
        for i in range(9):
            if flag[i] == 1:
                ans += a[i]
        if ans == 100:
            for i in range(9):
                if flag[i] == 1:
                    print(a[i])
            exit()
        return -1
    elif sum(flag) + 9 - n < 7:
        return -1

    flag[n] = 1
    dfs(n + 1,flag)
    flag[n] = 0
    dfs(n + 1, flag)


dfs(0,flag)