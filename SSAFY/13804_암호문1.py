from A.B import *
S(1, 'azder')

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(str,input().split()))
    stk = []
    for i in range(n-1,-1,-1):
        stk.append(numbers[i])

    n = int(input())
    order_list = list(map(str,input().split('I')))
    for i in range(1, n+1):
        order = order_list[i].split(' ')
        tmp = []
        for _ in range(int(order[1])):
            tmp.append(stk.pop())
        for k in range(int(order[2])):
            stk.append(order[-2-k])
        for _ in range(int(order[1])):
            stk.append(tmp.pop())

    print(f'#{test_case} ', end='')
    for i in range(10):
        print(stk.pop(),end=' ')
    print()
E(1, 'azder')
