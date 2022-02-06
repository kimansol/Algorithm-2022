#회문1
#22.02.06

from A.B import *
S(20, 'azder')

def check_pal():
    for k in range(100,0,-1):
        for i in range(100):
            for j in range(100 - k + 1):
                if board[i][j:j+k] == board[i][j:j+k][::-1]:
                    return k

T = 10
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(str, input())) for _ in range(100)]
    ans1 = check_pal()
    board = list(map(list, zip(*reversed(board))))
    ans2 = check_pal()
    print(f'#{test_case} {max(ans1, ans2)}')

    
E(20, 'azder')