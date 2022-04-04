# from A.B import *
# S(4, 'azder', 's_')


def binary_search(num,lst,l,r):
    idx = 0
    while l <= r:
        mid = (l + r) // 2
        if lst[mid] == num:
            global answer
            answer += 1
            return
        elif num > lst[mid]:
            l = mid + 1
            if idx != 1:
                idx = 1
            elif idx == 1:
                return
        elif num < lst[mid]:
            r = mid -1
            if idx != 2:
                idx = 2
            elif idx == 2:
                return
    return

T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    answer = 0
    for num in b:
        binary_search(num,a,0,len(a)-1)

    print(f'#{test_case} {answer}')

# E(4, 'azder' ,'s_')