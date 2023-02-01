### 문제

[2798번: 블랙잭](https://www.acmicpc.net/problem/2798)
<br><br>

### 문제 요약

카드 3장의 합→M을 넘지 않으면서 M과 최대한 가깝게 만들어야 함
<br><br>

### 슈도 코드

N,M 저장

lst로 요소 값 받기

ans = 0
<br><br>

i  0~끝-2

&nbsp;&nbsp;&nbsp;j 1~ 끝-1

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;k 2~끝

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;total = lst[i] + lst[j] + lst[k] 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;total ≤ M 이고 total > ans 면

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ans = total

print(ans)
<br><br>
### 배운 점

파이썬은 c++과 달리 chained comparison 가능

`if ans < total <= m`

다른 풀이

```python
#내 풀이
for i in range(0, n - 2):
    for j in range(1, n - 1):
        for k in range(2, n):
						if i == j or j == k or k == i:
                continue

#다른 풀이
for i in range(0, n - 2):
    for j in range(i+1, n - 1):
        for k in range(j+1, n):
```