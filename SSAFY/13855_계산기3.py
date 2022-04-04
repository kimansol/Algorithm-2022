from A.B import *
S(6, 'azder')


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n= int(input())
    str_list = list(input())
    stk = []
    post = ''
    op = {'(':0, '+':1, '*':2}


    for c in str_list:
        if c in ['0','1','2','3','4','5','6','7','8','9']:
            post += c
        elif c == ')':
            while stk[-1] != '(':
                post += stk.pop()
            stk.pop()
        elif c == '(':
            stk.append(c)
        else:
            while stk and op[stk[-1]] >= op[c]:
                post += stk.pop()
            stk.append(c)

    while stk:
        post += stk.pop()

    for s in post:
        if s == '+':
            stk.append(int(stk.pop()) + int(stk.pop()))
        elif s == '*':
            stk.append(int(stk.pop()) * int(stk.pop()))
        else:
            stk.append(s)
    print(f'#{test_case}', *stk)

E(6, 'azder')
