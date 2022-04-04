from A.B import *
S(2, 'azder')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    stk = []
    ans = 'Possible'
    cnt, timer = 0, 0

    while cnt < n:
        if timer !=0 and timer % m == 0:
            for i in range(k):
                stk.append(1)
        if timer in a:
            count = 0
            for time in a:
                if time == timer:
                    count += 1
            for i in range(count):
                if len(stk):
                    stk.pop()
                    cnt += 1
                else:
                    ans = 'Impossible'
                    break
        if ans == 'Impossible':
            break
        timer += 1

    print(f'#{test_case} {ans}')


E(2, 'azder')
