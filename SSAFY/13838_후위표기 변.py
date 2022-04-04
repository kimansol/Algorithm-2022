from A.B import *
S(17, 'azder', 's_')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str_list = list(input())
    stk = []
    print(f'#{test_case} ',end='')
    for s in str_list:
        if s == '+':
            if stk:
                if stk[-1] == '+':
                    print(stk.pop(),end='')
            stk.append(s)
        elif s == '*':
            stk.append(s)
        else:
            print(s,end='')
            if stk:
                if stk[-1] == '*':
                    print(stk.pop(), end='')
    if stk:
        print(stk.pop(), end='')
    print()



E(17, 'azder', 's_')
