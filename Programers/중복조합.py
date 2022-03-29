
def combinations_with_replacement(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations_with_replacement(arr[i:],r-1):
                yield [arr[i]] + next


a = list(combinations_with_replacement([0,1,2,3],2))
print(a)

def combinations(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r-1):
                yield [array[i]] + next
a = list(combinations([0,1,2,3],2))
print(a)

def permutations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next
a = list(permutations([0,1,2,3],2))
print(a)