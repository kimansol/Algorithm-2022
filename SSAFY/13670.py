
def subset():
    subsets = [[]]
    for num in numbers:
        size = len(subsets)
        for i in range(size):
            tmp = 0
            new_subset = subsets[i] + [num]
            for n in new_subset:
                tmp += n
            if tmp == 0:
                return 1
            subsets.append(new_subset)
    return 0


T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    ans = subset()
    print(f'#{test_case} {ans}')
