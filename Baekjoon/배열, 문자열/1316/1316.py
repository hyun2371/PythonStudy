def check(s):
    a = [] # 문자열에서 나온 문자 저장
    for i in range(len(s)):
        if s[i] not in a:  # 기존에 나온 문자가 아님
            a.append(s[i])
        elif i > 0 and s[i - 1] != s[i]:  # 기존에 나온 문자 && 불연속
            return False
    return True


cnt = 0
tries = int(input())

for _ in range(tries):
    st = input()
    if check(st) is True:
        cnt += 1

print(cnt)

