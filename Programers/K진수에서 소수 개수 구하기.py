# https://programmers.co.kr/learn/courses/30/lessons/92335
# # 2022카카오/레벨2/k진수에서 소수 개수 구하기
# 2022.02.19 / 25 시작 / 45 1번 시간초과 / 53 정답  28분
import math

def is_prime(num):
    if num == 1:
        return 0
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return 0
    return 1

def solution(n, k):
    answer = 0
    k_num = []
    while n >0:
        k_num.append(str(n%k))
        n //= k
    prime_list = ''.join(k_num[::-1]).split('0')
    print(prime_list)
    for num in prime_list:
        if num == '':
            continue
        if is_prime(int(num)):
            answer += 1
    return answer

print(solution(110011, 10))