#GNS
#22.02.06

from A.B import *

S(18, 'azder')

T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test_case1,n = map(str, input().split())
    numbers = list(map(str, input().split()))
    num_cnt = [0,0,0,0,0,0,0,0,0,0]
    num_cnt[0] = numbers.count('ZRO')
    num_cnt[1] = numbers.count('ONE')
    num_cnt[2] = numbers.count('TWO')
    num_cnt[3] = numbers.count('THR')
    num_cnt[4] = numbers.count('FOR')
    num_cnt[5] = numbers.count('FIV')
    num_cnt[6] = numbers.count('SIX')
    num_cnt[7] = numbers.count('SVN')
    num_cnt[8] = numbers.count('EGT')
    num_cnt[9] = numbers.count('NIN')
    num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    print(f'{test_case1}')
    for i in range(10):
        for j in range(num_cnt[i]):
            print(f'{num_str[i]}', end='')
            if i == 9 and j == num_cnt[i]:
                continue
            print(end=' ')
    print()


E(18, 'azder')