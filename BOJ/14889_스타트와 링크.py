# https://www.acmicpc.net/problem/14889
# 스타트와 링크/실버2/ 14899
# 2022.02.16

def calculate(start_team):
    link_team = []
    for i in range(n):
        if i not in start_team:
            link_team.append(i)
    global ans
    link_cnt = 0
    start_cnt = 0
    for i in range(n//2):
        for j in range(n//2):
            link_cnt += board[link_team[i]][link_team[j]]
            start_cnt += board[start_team[i]][start_team[j]]
    ans = min(ans, abs(link_cnt - start_cnt))



def select_team(cnt, start_team,idx):
    if cnt == n//2:
        calculate(start_team)
        return
    if n - idx + cnt <n//2:
        return

    start_team[cnt] = idx
    select_team(cnt+1,start_team,idx+1)
    start_team[cnt] = 0
    select_team(cnt, start_team, idx + 1)
    return


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
start_team = [-1] * (n//2)
ans =10e999

select_team(0,start_team,0)

print(ans)