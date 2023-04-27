import sys
b, n = sys.stdin.readline().split()
n = int(n)
result = 0
cnt = 0

for i in range(len(b)-1,-1,-1):
    if str(b[i]).isalpha():
        result += (ord(b[i]) - ord('A') + 10) * n ** cnt
    else:
        result += int(b[i]) * n ** cnt
    cnt += 1

print(result)