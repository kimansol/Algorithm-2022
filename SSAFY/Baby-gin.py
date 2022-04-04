from A.B import *
S(4, 'azder', 's_')

T = int(input())
for test_case in range(1, T + 1):
    numbers = str(input())

    a = [0] * 10
    for number in numbers:
        a[int(number)] += 1

    ans = 0
    for i in range(10):
        if a != 0:
            ans += a[i] // 3
            a[i] %= 3
            if i <= 7:
                while a[i] >= 1 and a[i + 1] >= 1 and a[i + 2] >= 1:
                    a[i] -= 1
                    a[i + 1] -= 1
                    a[i + 2] -= 1
                    ans += 1

    print(f'#{test_case} {1 if ans == 2 else 0}')


E(4, 'azder' ,'s_')