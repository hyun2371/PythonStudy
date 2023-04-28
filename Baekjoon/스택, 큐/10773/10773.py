import sys

stack = []
k = int(sys.stdin.readline())
for _ in range (k):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))