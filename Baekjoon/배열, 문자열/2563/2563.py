import sys
input = sys.stdin.readline
a = [[0] * 100 for _ in range(100)]


def paint(w, h):
    for i in range(w, w + 10):
        for j in range(h, h + 10):
            a[i][j] = 1


n = int(input())
for i in range(n):
    w, h = map(int, input().split())
    paint(w, h)

count = 0
for i in range(100):
    for j in range(100):
        if a[i][j] == 1:
            count += 1
print(count)

