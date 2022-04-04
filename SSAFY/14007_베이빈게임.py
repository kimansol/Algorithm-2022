from A.B import *
S(4, 'azder', 's_')

T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))

    a = [0] * 10
    b = [0] * 10
    ans = 0
    for i in range(6):
        a[numbers[i*2]] += 1
        if a[numbers[i*2]] ==3:
            ans = 1
            break
        for j in range(8):
            if a[j] !=0:
                if a[j+1] !=0 and a[j+2] != 0:
                    ans = 1
                    break
        if ans != 0:
            break

        b[numbers[i*2+1]] += 1
        if b[numbers[i*2+1]] ==3:
            ans = 2
            break
        for j in range(8):
            if b[j] !=0:
                if b[j+1] !=0 and b[j+2] != 0:
                    ans = 2
                    break
        if ans != 0:
            break

    print(f'#{test_case} {ans}')


E(4, 'azder' ,'s_')