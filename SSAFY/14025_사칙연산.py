from A.B import *
S(13, 'azder')

def post_order(cur_node):
   if cur_node <= n:
        if lc[cur_node]:
            post_order(lc[cur_node])
        if rc[cur_node]:
            post_order(rc[cur_node])
        if tree[cur_node] == '+':
            tree[cur_node] = int(tree[lc[cur_node]]) + int(tree[rc[cur_node]])
        elif tree[cur_node] == '*':
            tree[cur_node] = int(tree[lc[cur_node]]) * int(tree[rc[cur_node]])
        elif tree[cur_node] == '/':
            tree[cur_node] = int(tree[lc[cur_node]]) // int(tree[rc[cur_node]])
        elif tree[cur_node] == '-':
            tree[cur_node] = int(tree[lc[cur_node]]) - int(tree[rc[cur_node]])



for test_case in range(1, 11):
    n = int(input())
    lc = [0] * (n+1)
    rc = [0] * (n+1)
    tree = [0] * (n + 1)
    for i in range(n):
        tmp = list(map(str, input().split()))
        tree[int(tmp[0])] = tmp[1]
        if len(tmp) == 4:
            lc[int(tmp[0])] = int(tmp[2])
            rc[int(tmp[0])] = int(tmp[3])
    post_order(1)
    print(f'#{test_case} {int(tree[1])}')


E(13, 'azder')