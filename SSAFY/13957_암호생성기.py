from A.B import *
S(5, 'azder')

for test_case in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    while 1:
        for i in range(1,6):
            if lst[0] - i > 0:
                lst.append(lst.pop(0)-i)
            else:
                lst.pop(0)
                lst.append(0)
                break
        if lst[-1] == 0:
            break

    print(f'#{test_case}', *lst)

E(5, 'azder')