from A.B import *
S(17, 'azder', 's_')

T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test_case1,n = map(str, input().split())
    numbers = input().split()

    num_str = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    for number in numbers:
        num_str[number] += 1

    print(f'{test_case1}')
    for key, value in num_str.items():
        for _ in range(value):
            print(key, end=' ')
    print()

E(17, 'azder', 's_')