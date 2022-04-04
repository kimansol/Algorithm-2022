from A.B import *
S(25, 'azder', 's_')

def in_order(cur_node):
    global num
    if cur_node <= n:
        in_order(cur_node *2)
        tree[cur_node] = num
        num += 1
        in_order(cur_node *2 + 1)

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    tree = [0] * (n+1)
    num = 1
    in_order(1)

    print(f'#{test_case} {tree[1]} {tree[n//2]}')


E(25, 'azder', 's_')

