# https://www.acmicpc.net/problem/14696
# 백준14696/ 딱지놀이 / 브론즈1
# 2022.01.21

N = int(input())

for i in range(N):
    aa = list(map(int,input().split(' ')))[1:]
    bb = list(map(int,input().split(' ')))[1:]
    aa.sort(reverse=True)
    bb.sort(reverse=True)
    c = list(zip(aa,bb))
    for a,b in c:
        if a > b:
            print('A')
            break
        elif b > a:
            print('B')
            break
    else:
        if len(aa) > len(bb):
            print('A')
        elif len(bb) > len(aa):
            print('B')
        else:
            print('D')