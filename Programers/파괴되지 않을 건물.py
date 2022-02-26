#https://programmers.co.kr/learn/courses/30/lessons/92344
# 2022카카오/레벨3/파괴되지 않은 건물
# 2022.02.16 12:30/01:00
board =[[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

def solution(board, skill):
    tmp_board = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    answer = 0
    for t, r1, c1, r2, c2, d in skill:
        tmp_board[r1][c1] += d if t == 2 else -d
        tmp_board[r1][c2+1] -= d if t == 2 else -d
        tmp_board[r2+1][c1] -= d if t == 2 else -d
        tmp_board[r2+1][c2+1] += d if t == 2 else -d

    # for i in tmp_board:
    #     print(i)
    # print('---------------')

    for i in range(len(tmp_board)-1):
        for j in range(len(tmp_board[0])-1):
            if tmp_board[i][j] != 0:
                tmp_board[i][j+1] += tmp_board[i][j]
    # for i in tmp_board:
    #     print(i)
    # print('---------------')

    for j in range(len(tmp_board[0])-1):
        for i in range(len(tmp_board)-1):
            if tmp_board[i][j] != 0:
                tmp_board[i+1][j] += tmp_board[i][j]
    # for i in tmp_board:
    #     print(i)
    # print('---------------')

    for i in range(len(board)):
        for j in range(len(board[0])):
            if tmp_board[i][j] + board[i][j] > 0:
                answer += 1

    return answer


solution(board, skill)