n = int(input())
cnt = 0
cmp = 1

while True:
    if n <= cmp:
        break
    cnt += 1
    cmp += 6 * cnt

print(cnt + 1)
