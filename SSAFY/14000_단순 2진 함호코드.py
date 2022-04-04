from A.B import *
S(5, 'azder')
T = int(input())

hashtable=[
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1],

]

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input())) for _ in range(n)]

    answer = []
    for line in board:
        if any(line):
            for i in range(m-1,-1,-1):
                if line[i] == 1:
                    line = line[i-55:i+1]
                    break
            idx = 0
            for i in range(m - 6):
                if i < idx:
                    continue
                if line[i:i + 7] in hashtable:
                    for j in range(10):
                        if line[i:i + 7] == hashtable[j]:
                            answer.append(j)
                            break
                    idx += 6
                idx += 1
            break
    if len(answer) != 8:
        answer = 0
    else:
        if ((answer[0] + answer[2] + answer[4]+ answer[6])*3 + answer[1] + answer[3] + answer[5] +answer[7]) %10 != 0:
            answer = 0
        else:
            answer = sum(answer)
    print(f'#{test_case}',answer)
E(5, 'azder')