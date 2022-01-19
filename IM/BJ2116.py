#https://www.acmicpc.net/problem/2116
# 백준 2116/ 주사위 쌓기
# 2022.01.18

n = int(input()) ##주사위 갯수
dices = [list(map(int,input().split())) for _ in range(n)]

def findTop(x,dice):
    for i in range(6):
        if dice[i] == x:
            if i == 0:
                top = dice[5]
                front = max(dice[1], dice[2], dice[3], dice[4])
            elif i == 1:
                top = dice[3]
                front = max(dice[0], dice[2], dice[5], dice[4])
            elif i == 2:
                top = dice[4]
                front = max(dice[0], dice[1], dice[3], dice[5])
            elif i == 3:
                top = dice[1]
                front = max(dice[0], dice[2], dice[4], dice[5])
            elif i == 4:
                top = dice[2]
                front = max(dice[0], dice[1], dice[3], dice[5])
            else:
                top = dice[0]
                front = max(dice[1], dice[2], dice[3], dice[4])
            break
    return top, front

maxAns = 0
for i in range(1,7): ##맨 아래 6가지 경우 브루트포스
    bottom = i
    ans = 0
    for dice in dices:  #주사위 갯수만큼 쌓기
        bottom, front = findTop(bottom,dice)
        ans += front
    maxAns = max(ans, maxAns)

print(maxAns)
