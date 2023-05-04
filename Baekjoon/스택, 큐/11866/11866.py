from collections import deque

queue = deque()
result = []
n, k = map(int, input().split())
for i in range(n):
    queue.append(i+1)
for _ in range(n):
    for _ in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
print("<",end="")
print(*result,end="",sep=", ")
print(">")
