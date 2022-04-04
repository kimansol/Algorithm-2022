from A.B import *
S(6, 'azder', 'sample_')

import math
T = int(input())
for test_case in range(1, T+1):
    n = float(input())
    answer = ''
    for i in range(-1,-1,-1):
        if n >= 2**i:
            answer += '1'
            n -= 2**i
        else:
            answer += '0'
        if math.isclose(n,0):
            break

    if len(answer) > 12:
        answer = 'overflow'
    print(f'#{test_case} {answer}')

E(6, 'azder', 'sample_')