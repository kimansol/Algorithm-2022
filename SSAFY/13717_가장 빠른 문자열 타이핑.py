from A.B import *
S(2, 'azder', 'sample_')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1, str2 = map(list, input().split())
    ans = len(str1)
    str2_cnt = 0
    i = 0
    while i < len(str1)-len(str2)+1:
        if str1[i] == str2[0]:
            for j in range(1,len(str2)):
                if str1[i+j] != str2[j]:
                    i += 1
                    break
            else:
                str2_cnt += 1
                i += len(str2)
        else:
            i += 1

    print(f'#{test_case} {ans - (len(str2) -1) * str2_cnt}')

E(2, 'azder', 'sample_')