from A.B import *
S(2, 'azder', 's_')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = set(input())
    str2 = list(input())

    ans = 0
    for alpha in str1:
        tmp = 0
        for i in range(len(str2)):
            if alpha == str2[i]:
                tmp += 1
        if tmp > ans:
            ans =tmp

    print(f'#{test_case} {ans}')

E(2, 'azder', 's_')