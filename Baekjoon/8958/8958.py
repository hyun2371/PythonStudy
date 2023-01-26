n = int(input())
a = []
for _ in range(n):
    s = input()
    total = 0
    r = 0
    for i in range(0, len(s)):
        if s[i] == 'O':
            r += 1
        else:
            r = 0
        total += r
    a.append(total)

print(*a, sep="\n")
