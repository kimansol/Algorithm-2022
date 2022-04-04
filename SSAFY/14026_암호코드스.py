# from A.B import *
# S(5, 'azder', 'sample_')

xtob ={
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}
hashcode = {'112':0, '122':1, '221':2,'114':3, '231':4,'132':5, '411':6, '213':7, '312':8, '211':9}

def check(arr):
    if ((arr[7]+arr[5]+arr[3]+arr[1])*3 + arr[0]+arr[2]+arr[4]+arr[6]) % 10:
        return False
    return True

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [list(map(str, input())) for _ in range(n)]
    b_board = []
    for i in range(n):
        if i >= 1:
            if board[i] == board[i-1]:
                continue
        if len(set(board[i])) == 1:
            continue
        b_line = ''
        for char in board[i]:
            b_line += xtob[char]
        b_board.append(b_line)

    answer = 0
    for i in range(len(b_board)):
        ans = []
        f1 = f2 = f3 = 0
        for j in range(m * 4 - 1, -1, -1):
            if f2 == 0 and f3 == 0 and b_board[i][j] == '1':  # 첫 1
                f1 += 1
            elif f1 and f3 == 0 and b_board[i][j] == '0':  # 10
                f2 += 1
            elif f1 and f2 and b_board[i][j] == '1':  # 101
                f3 += 1
            elif f3 and b_board[i][j] == '0':
                mul = min(f1, f2, f3)
                ans.append(hashcode[str(f1 // mul) + str(f2 // mul) + str(f3 // mul)])
                f1 = f2 = f3 = 0
                if len(ans) == 8:
                    if check(ans):
                        answer = sum(ans)
                    ans = []
                if answer:
                    break
        if answer:
            break
    print(f'#{test_case} {answer}')
# E(5, 'azder', 'sample_')