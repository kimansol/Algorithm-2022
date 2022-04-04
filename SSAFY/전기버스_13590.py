from A.B import *
S(4, 'azder', 's_')

T = int(input())
for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    chargers = list(map(int, input().split()))
    stations = [0] * (n + 1)

    for chager in chargers:
        stations[chager] += 1
    station = cur_pos = ans = 0
    cur_pos += k

    while True:
        if cur_pos >= n:
            break
        if stations[cur_pos] == 1:
            ans += 1
            station = cur_pos
            cur_pos += k
        else:
            cur_pos -= 1
            if station == cur_pos:
                ans = 0
                break
    print(f'#{test_case} {ans}')

E(4, 'azder', 's_')
