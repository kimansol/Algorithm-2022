from A.B import *
S(28, 'azder', 's_')


def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    while p>=1 and tree[p] > tree[c]:
        tree[p],tree[c] = tree[c],tree[p]
        c = p
        p = c//2

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    last = 0
    tree = [0] * (n+1)

    for num in lst:
        enq(num)

    ans = 0
    while n>=1:
        n //=2
        ans += tree[n]

    print(f'#{test_case} {ans}')


E(28, 'azder', 's_')