
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    ans = 1
    stk = []
    for i in str1:
        if i == "{" or i == "(":
            stk.append(i)
        elif i == "}" or i == ")":
            if stk:
                a = stk.pop()
            else:
                ans = 0
                break
            if a == "{" and i == ")":
                ans = 0
                break
            if a == "(" and i == "}":
                ans = 0
                break
    if stk:
        ans = 0

    print(f'#{test_case} {ans}')
