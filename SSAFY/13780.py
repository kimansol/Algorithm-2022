from A.B import *
S(9, 'azder', 's_')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input_data = list(map(str, input()))
    ans = 1
    stk = []

    for data in input_data:
        if data == '(':
            stk.append(1)
        else:
            if len(stk) == 0:
                ans = 0
                break
            stk.pop()
    if len(stk) != 0:
        ans = 0

    print(f'#{test_case} {ans}')

E(9, 'azder', 's_')
