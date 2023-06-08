### 문제

https://www.acmicpc.net/problem/1417

<br>

### 문제 요약

입력

후보의 수

찍으려는 수 차례대로

출력

매수해야 하는 사람 최소값

<br>

### 슈도 코드

```
result = 0
list =[5,7,7]
list 역순으로
while !(max(list)!=list[0] and list.count(max(list))==1):
		max(list)-=1
		list[0]+=1
		result+=1
	
```

<br>

### 주의할 점

4 

10 10 10 10

경우에 max(list)가 0번이라 -1,+1 동시에 해줌 →무한 반복

이를 막기 위해 역순 정렬
