from collections import deque

queue = deque()
n = int(input())
for i in range(n):
    queue.append(i+1)
while True:
    if len(queue)==1:
        break
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])