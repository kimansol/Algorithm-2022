

def combinations_with_replacement(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations_with_replacement(arr[i:],r-1):
                yield [arr[i]] + next


a = list(combinations_with_replacement([0,1,2],2))
print(a)