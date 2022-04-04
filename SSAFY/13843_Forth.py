from A.B import *
S(19, 'azder', 's_')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str_list = list(input().split())
    stk = []
    ans = 0
    for i in str_list:
        if i == '.':
            ans = stk[0]
        elif i in ['+', '*', '/', '-']:
            if len(stk) <= 1:
                ans = 'error'
                break
            a = int(stk.pop())
            b = int(stk.pop())

            if i == '+':
                stk.append(a+b)
            elif i == '*':
                stk.append(a*b)
            elif i == '-':
                stk.append(b-a)
            else:
                stk.append(b//a)
        else:
            stk.append(i)
    if len(stk) != 1:
        ans = 'error'
    print(f'#{test_case} {ans}')


E(19, 'azder', 's_')