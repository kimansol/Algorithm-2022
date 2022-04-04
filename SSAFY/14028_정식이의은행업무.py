from A.B import *
S(6, 'azder', 'sample_')


T = int(input())
for test_case in range(1, T+1):
    n = str(input())
    num2 = int(n, 2)
    m = str(input())
    num3 = int(m, 3)
    ans = 0

    possible_value = []
    mul = 1
    for i in range(len(n)-1,-1,-1):
        if n[i] == '0':
            possible_value.append(num2 + mul)
        else:
            possible_value.append(num2 - mul)
        mul *= 2


    mul = 1
    for i in range(len(m) - 1, -1, -1):
        if m[i] == '0':
            if num3 + mul in possible_value:
                ans = num3 + mul
                break
            if num3 + mul * 2 in possible_value:
                ans = num3 + mul *2
                break
        elif m[i] == '1':
            if num3 + mul in possible_value:
                ans = num3 + mul
                break
            if num3 - mul in possible_value:
                ans = num3 - mul
                break
        else:
            if num3 - mul in possible_value:
                ans = num3 - mul
                break
            if num3 - mul * 2 in possible_value:
                ans = num3 - mul *2
                break
        mul *= 3

    print(f'#{test_case} {ans}')


E(6, 'azder', 'sample_')

