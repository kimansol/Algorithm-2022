#최대 성적표 만들기
#22.02.06

from tkinter.tix import Tree
from A.B import *

S(16, 'azder')

T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k= map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse=True)

    print(f'#{test_case} {sum(score[:k])}')
 
E(16, 'azder')