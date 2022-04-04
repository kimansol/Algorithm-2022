from A.B import *
S(0, 'azder')

T = int(input())
for test_case in range(1,T + 1):
    lst = list(map(int, input()))
    answer = []
    for i in range(0,len(lst)-1,7):
        tmp = 0
        tmp += lst[i] * (2**6)
        tmp += lst[i+1] * (2**5)
        tmp += lst[i+2] * (2**4)
        tmp += lst[i+3] * (2**3)
        tmp += lst[i+4] * (2**2)
        tmp += lst[i+5] * (2**1)
        tmp += lst[i+6] * (2**0)
        answer.append(tmp)

    print(f'#{test_case}',*answer)


E(0, 'azder')
