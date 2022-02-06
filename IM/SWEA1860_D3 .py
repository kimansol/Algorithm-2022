#진기의 최고급 붕어빵
#22.02.06

from matplotlib.pyplot import flag
from A.B import *
S(22, 'azder')


T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m,k = map(int, input().split())
    times = list(map(int, input().split()))
    times.sort()
    ans = 'Possible'
    bread = 0
    reserve = 0
    sold = 0
    time = 0
    flag = True
    while flag:
        if time != 0 and time % m == 0:
            bread += k
        while times[reserve] == time:
            bread -= 1
            sold += 1
            if bread < 0:
                ans = 'Impossible'
                flag = False
                break
            if sold == n:
                flag = False
                break
            reserve += 1
        time += 1
        

    print(f'#{test_case} {ans}')


E(22, 'azder')