#특별한 정렬
#22.02.06

from numpy import number
from A.B import *

S(4, 'azder')

T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    ans =[]
    numbers.sort()
    for i in range(5):
        ans.append(numbers[n-1-i])
        ans.append(numbers[i])

    print(f'#{test_case} ',end='')
    print(' '.join(map(str, ans)))

    

E(4, 'azder')