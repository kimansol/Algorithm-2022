#백만 장자 프로젝트
from A.B import *
S(8, 'azder', 's_')

T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    ans = 0
    cnt = 0
    max_val = 0
    for i in range(n):
        if numbers[i]>max_val:
            max_val = numbers[i]
    for i in range(n):
        if numbers[i] < max_val:
            ans -= numbers[i]
            cnt += 1
        elif numbers[i] == max_val:
            ans += numbers[i]*cnt
            cnt = 0
            max_val = 0
            for j in range(i+1,n):
                if numbers[j] > max_val:
                    max_val = numbers[j]


    print(f'#{test_case} {ans}')

E(8, 'azder', 's_')