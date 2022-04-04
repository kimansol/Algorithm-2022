from A.B import *
S(7, 'azder', 's_')

T = int(input())
for test_case in range(1, T + 1):
    p, pa, pb = map(int, input().split())
    al, ar= 1, p
    bl, br= 1, p
    while 1:
        ac = (al+ar)//2
        bc = (bl+br)//2
        if ac == pa or bc == pb:
            if ac != pa:
                print(f'#{test_case} B')
            elif bc != pb:
                print(f'#{test_case} A')
            else:
                print(f'#{test_case} 0')
            break

        if ac > pa:
            ar = ac-1
        else:
            al = ac+1

        if bc > pb:
            br = bc-1
        else:
            bl = bc+1

E(7, 'azder', 's_')