#작업 순서
#22.02.06

from collections import deque
from A.B import *

S(24, 'azder')


T = 10
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    sun = list(map(int, input().split()))
    parents = [[] for _ in range(v+1)]
    for i in range(0,len(sun),2):
        parents[sun[i+1]].append(sun[i])
    q = deque()
    ans = []
    for i in range(1,len(parents)):
        if len(parents[i]) == 0:
            ans.append(i)
        else:
            q.append((i,parents[i]))

    while q:
        idx, parent = q.popleft()
        for i in parent:
            if i not in ans:
                q.append((idx,parent))
                break
        else:
            ans.append(idx)

    print(f'#{test_case} ',end ='')
    print(' '.join(map(str, ans)))
    
E(24, 'azder')
