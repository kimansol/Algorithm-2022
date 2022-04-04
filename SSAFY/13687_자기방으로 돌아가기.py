#자기방으로 돌아가기
from A.B import *
S(6, 'azder', 'sample_')

T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    students = [list(map(int, input().split())) for _ in range(n)]
    st_path = [0] * 200
    for s,e in students:
        if s > e:
            s,e = e,s
        for i in range((s-1)//2,((e-1)//2)+1):
            st_path[i] += 1
    ans = 0
    for path in st_path:
        if path > ans:
            ans = path
    print(f'#{test_case} {ans}')

E(6, 'azder', 'sample_')