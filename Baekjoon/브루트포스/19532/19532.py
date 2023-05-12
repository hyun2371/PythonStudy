import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split())

for i in range(-999, 999+1):
    for j in range(-999, 999+1):
        if a * i + b * j == c and d * i + e * j == f:
            x ,y = i, j
            break

print(x, y)