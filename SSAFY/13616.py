#간단한 소인수 분해
from A.B import *
S(0, 'azder')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    ans = [0,0,0,0,0]
    while n%2 == 0:
        n = n//2
        ans[0] += 1
    while n%3 == 0:
        n = n//3
        ans[1] += 1
    while n%5 == 0:
        n = n//5
        ans[2] += 1
    while n%7 == 0:
        n = n//7
        ans[3] += 1
    while n%11 == 0:
        n = n//11
        ans[4] += 1
    print(f'#{test_case}',end=' ')
    print(*ans)

E(0, 'azder')