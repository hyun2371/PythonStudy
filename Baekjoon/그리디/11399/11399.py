import sys

n = int(input())
t = list(map(int,sys.stdin.readline().split()))

t.sort()

result = 0
for i in range(len(t)):
    for j in range(0,i+1):
        result+=t[j]

print(result)