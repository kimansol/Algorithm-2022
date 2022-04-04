from A.B import *
S(0, 'azder', 's_')

def quick(data, left, right):
  if left >= right:
    return

  pivot=data[left]

  l = left
  r = right
  while l <= r:
    while pivot > data[l]:
      l = l+1
    while pivot < data[r]:
      r = r-1

    if l <= r:
      data[l], data[r] = data[r], data[l]
      l, r = l+1, r-1

  quick(data, left, l-1)
  quick(data, l, right)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    quick(numbers, 0, len(numbers) - 1)

    print(f'#{test_case} {numbers[n//2]}')

E(0, 'azder' ,'s_')