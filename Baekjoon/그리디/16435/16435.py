import sys
n, l = map(int, sys.stdin.readline().split())

h = list(map(int,sys.stdin.readline().split()))
h.sort()

for i in range(n):
    if l < h[i]:
        break
    else:
        l += 1

print(l)