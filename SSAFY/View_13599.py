T = 10
for test_case in range(1, T + 1):
    n = int(input())
    board = list(map(int, input().split()))
    ans = 0
    for i in range(2, n-2):
        max_heigh = 0
        if board[i-2] > max_heigh:
            max_heigh = board[i-2]
        if board[i-1] > max_heigh:
            max_heigh = board[i-1]
        if board[i+2] > max_heigh:
            max_heigh = board[i+2]
        if board[i+1] > max_heigh:
            max_heigh = board[i+1]
        if board[i] > max_heigh:
            ans += board[i] - max_heigh

    print(f'#{test_case} {ans}')