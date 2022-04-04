from A.B import *
S(1, 'azder')

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
    for i in range(0,len(blst),7):
        tmp = blst[i:i+7]
        onum = 0
        multi = 1
        for i in range(len(tmp)-1,-1,-1):
            onum += tmp[i] * multi
            multi *= 2
        answer.append(onum)
    print(f'#{test_case}',*answer)


E(1, 'azder')
