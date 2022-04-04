from A.B import *
S(5, 'azder', 'sample_')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sentence = input()

    tmp1 = []
    tmp2 = []
    for alpha in sentence:
        if alpha not in tmp1:
            tmp1.append(alpha)
        elif alpha not in tmp2:
            tmp2.append(alpha)


    if len(tmp1) == 2 and len(tmp2) == 2:
        ans = 'Yes'
    else:
        ans = 'No'
    print(f'#{test_case} {ans}')

E(4, 'azder', 'sample_')
