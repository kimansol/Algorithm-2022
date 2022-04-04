from A.B import *
S(3, 'azder', 's_')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int,input().split()))

    #선택정렬
    for i in range(n):
        tmp = i
        for j in range(i+1,n):
            if numbers[tmp] > numbers[j]:
                tmp = j
        numbers[i],numbers[tmp] = numbers[tmp],numbers[i]

    print(f'#{test_case} ',end='')
    for i in range(5):
        print(numbers[-1 - i], end=' ')
        print(numbers[i], end=' ')
    print()

E(3, 'azder', 's_')