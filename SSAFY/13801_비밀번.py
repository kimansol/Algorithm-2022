from A.B import *
S(13, 'azder', 's_')


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, password = map(str, input().split())
    stk = []
    for num in password:
        if len(stk) == 0:
            stk.append(num)
        elif stk[-1] == num:
            stk.pop()
        else:
            stk.append(num)

    print(f'#{test_case} ',end='')
    print(''.join(stk))

E(13, 'azder', 's_')