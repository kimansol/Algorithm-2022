# from A.B import *
# S(21, 'azder', 's_')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,k = map(int, input().split())
    lst = list(map(int, input().split()))
    stk = []
    ans = 0
    stk.append([0, 1])
    stk.append([lst[0], 1])

    while stk:
        hap, idx = stk.pop()
        if hap == k:
            ans += 1
            continue
        if idx == n or hap > k:
            continue
        stk.append([hap+lst[idx], idx +1])
        stk.append([hap,idx + 1])

    print(f'#{test_case} {ans}')

#
# E(21, 'azder', 's_')