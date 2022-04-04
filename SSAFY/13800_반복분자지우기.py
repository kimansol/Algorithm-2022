from A.B import *
S(12, 'azder', 's_')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str_list = list(input())
    stk = []
    for alpha in str_list:
        if len(stk) == 0:
            stk.append(alpha)
        elif alpha == stk[-1]:
            stk.pop()
        else:
            stk.append(alpha)

    print(f'#{test_case} {len(stk)}')


E(12, 'azder', 's_')
