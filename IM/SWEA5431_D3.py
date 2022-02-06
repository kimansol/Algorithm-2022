#민석이의 과제 체크하기
#22.02.06

from A.B import *

S(3, 'azder')

T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    m, k = map(int ,input().split())
    students = list(map(int, input().split()))
    ans =[]
    for student in range(1,m+1):
        if student not in students:
            ans.append(student)

    print(f'#{test_case} ',end='')
    print(' '.join(map(str, ans)))

    

E(3, 'azder')