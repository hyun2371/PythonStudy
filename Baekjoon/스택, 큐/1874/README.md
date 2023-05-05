### 문제

[https://www.acmicpc.net/problem/1874](https://www.acmicpc.net/problem/1874)

<br>

### 문제 요약

입력

첫 줄 n 

두번째 ~n번째 → 1~ n 수열

출력

push pop 연산으로 수열을 만들 수 있는지 여부

<br>

### 슈도 코드

```
for i in range(1, 4+1):
	push(i)
pop(4)
pop(3)

for i in range(5, 6+1):
	push(i)
pop(6)

for i in range(7, 8+1):
	push(i)
pop(8)
pop(7)
```

<br>

```
count = 0

k = 4
for i in range(count,k)
	push(i+1)
	count++
pop(k)

if k > count
	 for i in range(1, k+1)
			push(i)
			count++
		pop(k)

else
	if stack.peek() != k
		break
	pop(k)

```