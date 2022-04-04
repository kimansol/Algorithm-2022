from A.B import *
S(2, 'azder')

hashtable=[
    [0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1],
]


T = int(input())
for test_case in range(1,T + 1):
    xlst = list(map(str, input()))
    blst = []
    for xnum in xlst:
        if ord(xnum) >= 65:
            xnum = ord(xnum)-55
        tmp = []
        xnum = int(xnum)
        for _ in range(4):
            tmp.append(xnum%2)
            xnum //= 2
        blst.extend(tmp[::-1])

    answer = []
    idx = 0
    for i in range(len(blst)-5):
        if i < idx:
            continue
        if blst[i:i+6] in hashtable:
            for j in range(10):
                if blst[i:i+6] == hashtable[j]:
                    answer.append(j)
                    break
            idx += 5
        idx += 1
    print(f'#{test_case}',*answer)


E(2, 'azder')
