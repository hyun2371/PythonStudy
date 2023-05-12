### 문제

[https://www.acmicpc.net/problem/19532](https://www.acmicpc.net/problem/19532)

<br>

### 문제 요약

$ax+ by = c$

$dx+ ey = f$

-999 ≤ x,y ≤ 999

a, b, c, d, e, f 주어짐

만족하는 x,y 구하기

<br>

### 슈도 코드

```plain
for i -999 ~ 999
	for j -999 ~ 999
		if a * i + b * j == c and d * i + e * j ==  f
				x = i and y = j
				break
```