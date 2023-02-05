### 문제

[2563번: 색종이](https://www.acmicpc.net/problem/2563)
<br><br>

### 문제 요약

100x100의 도화지

그 위로 n장의 색종이(10x10)를 평행하게 붙임

색종이가 붙은 영역의 넓이를 계산하기
<br><br>


**입력**

색종이 개수

색종이 왼쪽 변과 도화지 사이 거리

색종이의 아래족변과 도화지 사이의 거리

→왼쪽 아래 꼭짓점 좌표
<br><br>

### 슈도 코드

```
#색종이 영역만큼 1로 색칠#

for i in range(x,x+10):
	for j in range(y,y+10):
		a[i][j] =1

#1로 색칠한 곳 카운트#

for i in range(100):
	for j in range(100):
		if (a[i][j] ==1):
			count+=1
```
<br><br>
### 배운 점

```python
input()
# 같음
import sys
sys.stdin.readline()
```