from A.B import *
S(26, 'azder', 's_')

def post_order(cur_node):
    if cur_node <= (e+2):
        if lc[cur_node] and lc[cur_node] <= (e+2):
            post_order(lc[cur_node])
        if rc[cur_node] and rc[cur_node] <= (e+2):
            post_order(rc[cur_node])

        if lc[cur_node] == 0 and rc[cur_node] == 0:
            count_tree[cur_node] = 1
        else:
            count_tree[cur_node] = count_tree[lc[cur_node]] + count_tree[rc[cur_node]] +1

T = int(input())
for test_case in range(1, T+1):
    e,n = map(int, input().split())
    edge_lst = list(map(int, input().split()))
    answer = 0

    p = [0] * (e + 2)
    lc = [0] * (e+2)
    rc = [0] * (e+2)
    for i in range(e):
        if lc[edge_lst[i*2]] == 0:
            lc[edge_lst[i*2]] = edge_lst[i*2+1]
        else:
            rc[edge_lst[i*2]] = edge_lst[i*2+1]
        p[edge_lst[i*2+1]] = edge_lst[i*2]
    for i in range(1,e+2):
        if p[i] == 0:
            root = i
            break

    count_tree=[0] * (e+2)
    post_order(root)

    print(f'#{test_case} {count_tree[n]}')

E(26, 'azder', 's_')