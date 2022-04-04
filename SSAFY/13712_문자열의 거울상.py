from A.B import *
S(16, 'azder', 's_')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sentence = list(map(str, input()))
    print(f'#{test_case} ', end='')
    for i in range(len(sentence)-1,-1,-1):
        if sentence[i] == 'q':
            print('p', end='')
        elif sentence[i] == 'p':
            print('q', end='')
        elif sentence[i] == 'b':
            print('d', end='')
        elif sentence[i] == 'd':
            print('b', end='')
    print()

E(16, 'azder', 's_')
