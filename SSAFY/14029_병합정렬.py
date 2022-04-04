from A.B import *
S(2, 'azder', 's_')

def merge_sort(numbers):
    global answer
    n = len(numbers)
    if n <= 1:
        return
    mid = n // 2
    left_group = numbers[:mid]
    right_group = numbers[mid:]

    merge_sort(left_group)
    merge_sort(right_group)

    left = 0
    right = 0
    now = 0

    while left < len(left_group) and right < len(right_group):
        if left_group[left] < right_group[right]:
            numbers[now] = left_group[left]
            left += 1
            now += 1
        else:
            numbers[now] = right_group[right]
            right += 1
            now += 1

    while left < len(left_group):
        numbers[now] = left_group[left]
        left += 1
        now += 1

    while right < len(right_group):
        numbers[now] = right_group[right]
        right += 1
        now += 1

    if left_group[-1] > right_group[-1]:
        answer += 1


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    answer = 0
    numbers = list(map(int, input().split()))
    merge_sort(numbers)

    print(f'#{test_case} {numbers[n//2]} {answer}')

E(2, 'azder', 's_')