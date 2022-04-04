from A.B import *
S(6, 'azder')

def intopost(lst):
    post = []
    stk = []
    op = {'(': 0, '+': 1, '*': 2}

    for c in lst:
        if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            post.append(c)
        elif c == ')':
            while stk[-1] != '(':
                post.append(stk.pop())
            stk.pop()
        elif c == '(':
            stk.append(c)
        else:
            while stk and op[stk[-1]] >= op[c]:
                post.append(stk.pop())
            stk.append(c)

    while stk:
        post.append(stk.pop())

    return post

def post_cal(post):
    stk = []
    for s in post:
        if s == '+':
            stk.append(int(stk.pop()) + int(stk.pop()))
        elif s == '*':
            stk.append(int(stk.pop()) * int(stk.pop()))
        else:
            stk.append(s)

    return stk


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n= int(input())
    str_list = list(input())

    post = intopost(str_list)
    stk = post_cal(post)

    print(f'#{test_case}', *stk)

E(6, 'azder')