### 문제

[2581번: 소수](https://www.acmicpc.net/problem/2581)
<br><br>

### 문제 요약

첫째줄에 M, 둘째줄에 N이 주어짐

M과 N은 10000이하의 자연수이며

소수인 것을 모두 찾아 첫 째줄에 합, 둘째줄에 최소값 출력

M~N사이 소수가 없으면 -1 출력
<br><br>

### 슈도 코드

<b>소수 판별 함수</b>

def check_p(n):
    
if n == 1:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;소수 x

for i in  range 0~루트(n):

&nbsp;&nbsp;&nbsp;&nbsp;if n % i == 0

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;소수 x

소수 o
<br><br>

startN, endN 입력 받기

p_lst = []

for n in range startN~ endN:

&nbsp;&nbsp;&nbsp;&nbsp;if check_p(n):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p_lst에 추가
<br><br>

if p_lst 길이 = 0

&nbsp;&nbsp;&nbsp;&nbsp;print(-1)

else p_lst  p_lst 합 출력, 첫 번째 요소 출력
<br><br>

### 테스트

20 29
→ 52, 23 출력

1
→-1 출력