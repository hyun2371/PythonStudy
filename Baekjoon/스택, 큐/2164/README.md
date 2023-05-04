### 문제

[https://www.acmicpc.net/problem/2164](https://www.acmicpc.net/problem/2164)

<br>

### 문제 요약

1번 카드 제일 위에

n번 카드 제일 아래

카드 한 장 남을 때까지 반복

1. 제일 위에 있는 카드 버림
2. 제일 위의 카드를 카드 밑으로

제일 마지막에 남는 카드 출력

<br>

### 슈도 코드

```
for i in range(n):
	queue.append(i+1)

while len(queue)>1:
	queue.popleft()
	queue.append(queue.popleft())

print(queue[0])
```