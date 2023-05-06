import sys
from collections import deque

deq = deque()
n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    deq.append(i + 1)

key = sys.stdin.readline().split()
cnt = 0

for i in range(m):
    k = int(key[i])
    if deq.index(k)<= len(deq) // 2:
        while deq.index(k) != 0:
            deq.append(deq.popleft())  # 왼쪽 이동
            cnt += 1
        deq.popleft() # 2번연산
    else:
        while deq.index(k) != 0:
            deq.appendleft(deq.pop()) # 오른쪽 이동
            cnt += 1
        deq.popleft() # 3번 연산

print(cnt)