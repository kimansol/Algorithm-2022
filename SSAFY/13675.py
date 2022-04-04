from A.B import *
S(2, 'azder', 's_')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def func(idx,cnt,flag,hap):
    global ans
    if cnt == n:
        if hap == k:
            ans += 1
        return
    if 12 - idx + cnt < n:
        return

    flag[idx] = 1
    func(idx+1,cnt+1,flag, hap + idx+1)
    flag[idx] = 0
    func(idx + 1, cnt, flag, hap)
    return

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    ans = 0
    flag = [0] * 12
    func(0,0,flag,0)

    print(f'#{test_case} {ans}')

E(2, 'azder', 's_')