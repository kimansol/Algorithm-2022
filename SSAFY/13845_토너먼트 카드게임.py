from A.B import *
S(22, 'azder', 's_')

T = int(input())

def play(s,e):
    if s == e:
        return s

    left = play(s,(s+e)//2)
    right = play((s+e)//2+1,e)

    if (lst[left]+1)%3 == lst[right]%3:
        return right
    else:
        return left

for test_case in range(1,T + 1):
    n = int(input())
    lst = [0] + list(map(int, input().split()))
    ans = play(1,n)
    print(f'#{test_case} {ans}')


E(22, 'azder', 's_')
