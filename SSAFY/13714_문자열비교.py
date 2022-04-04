from A.B import *
S(0, 'azder', 's_')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())
    ans = 0
    for i in range(len(str2)-len(str1)+1):
        if str2[i] == str1[0]:
            for j in range(1,len(str1)):
                if str2[i+j] != str1[j]:
                    break
            else:
                ans = 1
                break
    print(f'#{test_case} {ans}')


E(0, 'azder', 's_')
