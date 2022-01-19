#https://www.acmicpc.net/problem/1244
#백준 1244/ 스위치 켜고 끄기
# 2022.01.18

n = int(input()) #스위치 갯수
status = list(map(int,input().split(' ')))

sn = int(input()) ##사람수
slist = [list(map(int,input().split())) for _ in range(sn)]

for sex, num in slist:
    if sex == 1: ##남자
        tmp = num -1
        while tmp<n:
            status[tmp] = not status[tmp]
            tmp += num
        pass
    else: #여자
        num -= 1
        status[num] = not status[num]
        index = 1
        while 1:
            if num-index < 0 or num+index >= n:
                break
            if status[num-index] == status[num+index]:
                status[num-index] = not status[num-index]
                status[num+index] = not status[num+index]
                index += 1
            else:
                break

for i in range(len(status)):
    if status[i] == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')
    if i > 0 and (i+1) % 20 == 0:
        print('')


