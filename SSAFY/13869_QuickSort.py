from A.B import *
S(3, 'azder')

def quick_sort(s,e):
    if s >= e:
        return

    t = s
    p = e
    for i in range(s,e):
        if lst[i] < lst[p]:
            lst[i],lst[t] = lst[t],lst[i]
            t+=1
    lst[p], lst[t] = lst[t], lst[p]
    p = t

    quick_sort(s,p-1)
    quick_sort(p+1,e)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int ,input().split()))
    quick_sort(0, n-1)
    print(f'#{test_case}',*lst)

E(3, 'azder')
