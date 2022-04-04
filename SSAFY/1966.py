from A.B import *
S(0, 'azder')
#버블
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    for i in range(n-1):
        for j in range(1,n-i):
            if numbers[j-1] >= numbers[j]:
                temp = numbers[j-1]
                numbers[j-1] = numbers[j]
                numbers[j] = temp

    print(f'#{test_case} ', end='')
    print(*numbers)

E(0, 'azder')