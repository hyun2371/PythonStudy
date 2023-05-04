### 문제

[https://www.acmicpc.net/problem/11866](https://www.acmicpc.net/problem/11866)

<br>

### 문제 요약

1~N n명

순서대로 k번째 사람을 제거

7 6 5 4 3 2 1

→ 2 1 7 6 5 4          <3

→  5 4 2 1 7   <3, 6>

→ 1 7 5 4   <3, 6, 2>

→ 5 4 1    <3, 6, 2, 7>

→ 4 1  <3, 6, 2, 7, 5>

→ 4     <3, 6, 2, 7, 5, 1>

<3, 6, 2, 7, 5, 1, 4>

<br>

### 슈도 코드

```
result=[]
queue.push(1~n)

n만큼 반복:
	k-1만큼 반복:
		queue.push(pop())
	queue.pop() → result에 저장

result 출력
```