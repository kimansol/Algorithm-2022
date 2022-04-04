from A.B import *
S(3, 'azder')


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    target = list(map(str, input()))
    sentence = list(map(str, input()))
    ans = 0
    for i in range(len(sentence)-len(target)+1):
        if sentence[i] == target[0]:
            for j in range(1,len(target)):
                if sentence[i+j] != target[j]:
                    break
            else:
                ans += 1

    print(f'#{test_case} {ans}')

E(3, 'azder')
