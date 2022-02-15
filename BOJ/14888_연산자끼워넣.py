#https://www.acmicpc.net/problem/14888
#14888/실버1/연산자끼워넣기
#2022.02.15   #8:30 #9:00틀렸습니다 #9:20 max = -10e999 안함

def calculate(flag):
    global max_val, min_val
    tmp = numbers[0]
    idx = 1
    for operator in flag:
        if operator == 0:
            tmp += numbers[idx]
        elif operator == 1:
            tmp -= numbers[idx]
        elif operator == 2:
            tmp *= numbers[idx]
        else:
            if tmp >= 0:
                tmp //= numbers[idx]
            else:
                tmp = -(-tmp//numbers[idx])
        idx +=1
    min_val = min(min_val, tmp)
    max_val = max(max_val, tmp)


def back(cnt, flag,operators):
    if cnt == n-1:
        calculate(flag)
        return

    for i in range(4):
        if operators[i]:
            flag[cnt] = i
            operators[i] -= 1
            back(cnt+1,flag,operators)
            flag[cnt] = i
            operators[i] += 1
    return

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_val = -10e999
min_val = 10e999


flag = [-1] * (n-1)
ans = 0
back(0, flag, operators)

print(max_val)
print(min_val)