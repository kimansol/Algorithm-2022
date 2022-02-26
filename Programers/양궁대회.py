# https://programmers.co.kr/learn/courses/30/lessons/92342
# 2022카카오/레벨2/양궁
# 2022.02.24 # 02:33

def combinations_with_replacement(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations_with_replacement(arr[i:],r-1):
                yield [arr[i]] + next

def solution(n, info):
    score = [-1, 10, 0, [-1]] # 최고점, 최저점, 최저점을 쏜 횟수, 점수 목록
    for lst in list(combinations_with_replacement([10,9,8,7,6,5,4,3,2,1,0],n)): #[10,10,10,10,10] - > [0,0,0,0,0] 11Hn
        lion = 0
        apeach = 0
        for i in range(11): # 10점부터 0점까지 쏜 횟수를 비교하며 점수 계산
            if info[i] and (info[i] >= lst.count(10-i)):
                apeach += (10 - i)
            elif lst.count(10-i) and info[i] < lst.count(10-i):
                lion += (10 -i)
        if lion > apeach:
            if lion - apeach > score[0]: #점수차가 최고보다 더클떄
                score[0] = lion - apeach
                score[1] = min(lst)
                score[2] = lst.count(min(lst))
                score[3] = lst
            elif lion - apeach == score[0]: #라이언 점수가 최고값과 같을때
                if min(lst) < score[1]: #최소점수를 비교
                    score[1] = min(lst)
                    score[2] = lst.count(min(lst))
                    score[3] = lst
                elif min(lst) == score[1]: # 최소 점수가 같을때는 최소점수에 쏜 횟수를 비교
                    if lst.count(min(lst)) > score[2]:
                        score[2] = lst.count(min(lst))
                        score[3] = lst

    if score[3] != [-1]:
        answer = [0] * 11
        for num in score[3]:
            answer[num] += 1
    else:
        answer = score[3]
    return answer[::-1]

print(solution(10,[1,1,2,2,1,1,1,1,0,0,0]))