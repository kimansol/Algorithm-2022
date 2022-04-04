from A.B import *
S(19, 'azder', 'sample_')

def in_order(cur_node):
    global num
    if cur_node <= 1000000:
        left_node = cur_node *2
        if left_node <= 1000000:
            in_order(left_node)
        tree[cur_node] = num
        num += 1
        right_node = cur_node * 2 + 1
        if right_node <= 1000000:
            in_order(right_node)

def search(cur_node):
    while cur_node <= 1000000:
        if tree[cur_node] ** 3 == n:
            return tree[cur_node]
        elif tree[cur_node] ** 3 > n:
            cur_node = cur_node *2
        else:
            cur_node = cur_node * 2 + 1
    return -1


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    tree = [0] * (1000001)
    num = 1
    in_order(1)
    print(f'#{test_case} {search(1)}')

E(19, 'azder', 'sample_')