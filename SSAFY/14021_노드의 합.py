from A.B import *
S(27, 'azder', 's_')


def post_order(cur_node):
    if cur_node <= n:
        left_node, right_node = cur_node*2,cur_node*2+1
        if left_node <=n:
            post_order(left_node)
        if right_node <= n:
            post_order(right_node)
        if cur_node * 2 <=n:
            tree[cur_node] += tree[left_node]
        if cur_node * 2 + 1 <= n:
            tree[cur_node] += tree[right_node]


T = int(input())
for test_case in range(1, T+1):
    n,m,l = map(int, input().split())
    tree = [0] * (n+1)
    for i in range(m):
        idx, num = map(int ,input().split())
        tree[idx] = num

    post_order(l)

    print(f'#{test_case} {tree[l]}')


E(27, 'azder', 's_')