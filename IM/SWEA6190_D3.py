#정곤이의 단조 증가하는 수
#22.02.06

from A.B import *

S(17, 'azder')

def check_danjo(n):
    num = 10
    while n:
        if n%10 > num:
            return 0
        num = n %10
        n = n// 10
    return 1

T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    ans = -1
    for i in range(n-1):
        for j in range(i+1,n):
            if check_danjo(numbers[i]*numbers[j]):
                ans = max(ans, numbers[i]*numbers[j])
    print(f'#{test_case} {ans}')


E(17, 'azder')