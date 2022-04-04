from A.B import *
S(3, 'azder', 's_')

T = int(input())
for test_case in range(1, T + 1):
    n, m= map(int ,input().split())
    answer = 'OFF'
    b_n = ''
    while m > 0:
        b_n += str(m%2)
        m //= 2
    if b_n == '':
        b_n = '0'
    if all(list(map(int, b_n[0:n]))):
        answer = 'ON'
    print(f'#{test_case} {answer}')


E(3, 'azder', 's_')