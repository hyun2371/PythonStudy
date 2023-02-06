import sys
n = int(sys.stdin.readline())

ans = 0
cnt = 0
while True:
    if "666" in str(ans):
        cnt += 1
    if cnt == n:
        break
    ans += 1

print(ans)

