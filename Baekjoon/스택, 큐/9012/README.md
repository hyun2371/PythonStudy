### 문제

[https://www.acmicpc.net/problem/9012](https://www.acmicpc.net/problem/9012)

<br>

### 문제 요약

PS 괄호기호로만 구성된 문자열

VPS 한 쌍의 괄호 기호로 된 () 문자열 

x가 VPS면 (x)로 VPS, VPS끼리 연결도 VPS

VPS? YES : NO

<br>

### 슈도 코드

( → push x

) → pop()

<br>

VPS가 아닌 조건

- 비었는데 ) 이 옴 = 비어있는데 pop을 함
- 마지막에 x가 남아있음 = 스택이 비어있지 않음

<br>


```
n만큼 반복
	s 입력받기
	isVPS(s)

def isVPS(s)

for i in range(len(s)):
	s[i] == '(' -> stack.append('x')

	s[i] == ')'  ->
		stack.isEmpty() ->return "NO"
					    ->stack.pop()
	

if !s.isEmpty() ->return "NO"
else -> return "YES"
```