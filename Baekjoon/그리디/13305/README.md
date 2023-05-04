### 문제

[https://www.acmicpc.net/problem/13305](https://www.acmicpc.net/problem/13305)

<br>

### 문제 요약

N개의 도시들이 수평 방향으로 있음

맨 왼쪽에서 맨 오른쪽으로 이동

1km마다 1L 기름

각 도시마다 1L당 기름값 다름

기름값 최소 비용 구하기

<br>


**입력**

도시 개수

각 도시 연결하는 도로 길이

각 도시의 기름 가격

<br>


**출력**

기름값 최소 비용

<br>


### 슈도 코드

5 → 기름 없음 다음 도시까지 2L 기름 필요

2L 충전

2→ 3L 기름 필요 다음 도시 기름이 더 비쌈 다음에서 다다음 가는 1L충전

3L + 1L 충전

```
두번째~ 끝-1 까지 반복 i
	두번째~i까지 최소 뽑기
가격 = 최소값 * 길이

result = 0
price = [5, 2, 4, 1]
length = [2, 3, 1]

min= price[0]
result = price * length[0]

for i in range (1, n-1):   //1,2
	if price[i]< min:
		min = price[i]
	result+=length[i] * min
```