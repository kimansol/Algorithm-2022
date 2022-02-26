# https://programmers.co.kr/learn/courses/30/lessons/92341
# 2022카카오/레벨2/주차 요금 계산
# 2022.02.24 # 40분

def solution(fees, records):
    car = {}
    #{'5961': ['05:34', '07:59', '22:59', '23:00'], '0000': ['06:00', '06:34', '18:59'], '0148': ['07:59', '19:09']}
    for record in records:
        if car.get(record.split()[1]) == None:
            car[record.split()[1]] = [record.split()[0]]
        else:
            car[record.split()[1]].append(record.split()[0])

    #['0000', '0148', '5961']
    answer = sorted(list(car.keys()))
    for i in range(len(answer)):
        log = car[answer[i]] # ['06:00', '06:34', '18:59']
        time = 0
        for j in range(0,len(log),2): #시간:분 -> 분으로 전환 06:00 -> 360, 06:34->394
            if j+1 < len(log): #짝수일떄
                time += (int(log[j+1][0:2])*60 + int(log[j+1][3:5])) - (int(log[j][0:2])*60 + int(log[j][3:5]))
            else: #홀수일떄  23:59 -> 1439
                time += 1439 - (int(log[j][0:2])*60 + int(log[j][3:5]))

        if time <= fees[0]: # 기준시간보다 적을때
            answer[i] = fees[1]
        else: # 기준시간보다 많을때
            answer[i] = fees[1] + (((time)-fees[0])//fees[2]) * fees[3]
            if ((time)-fees[0])%fees[2] != 0: # 올림 값 계산
                answer[i] += fees[3]

    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))