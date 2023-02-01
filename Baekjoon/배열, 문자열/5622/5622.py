s = input()

t = 0
for i in s:
    n = ord(i) - ord('A')
    if n // 3 == 0:
        t += 3
    elif n // 3 == 1:
        t += 4
    elif n // 3 == 2:
        t += 5
    elif n // 3 == 3:
        t += 6
    elif n // 3 == 4:
        t += 7
    elif n // 3 == 5 or n == 18:
        t += 8
    elif n // 3 == 6 or n == 21:
        t += 9
    else:
        t += 10
print(t)

# 다이얼 원소 하나씩 추출