### 문제

[11653번: 소인수분해](https://www.acmicpc.net/problem/11653)
<br><br>

### 문제 요약

N이 주어질 때, 소인수분해 결과를 한줄씩 오름차순으로 출력

N==1 → 출력 x 
<br><br>

### 슈도 코드

n 입력 받기

i = 2

while i≤n

&nbsp;&nbsp;if n % i == 0  &nbsp;&nbsp;&nbsp;#i가 n의 소인수

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n = n // i

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i 출력

&nbsp;&nbsp;else

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i ++
<br><br>

### 배운점

소인수분해 72

- 2로 계속 나눈 다음 3으로 나눔→i 순차적으로 더해도 상관없음
- 4로 나눠져도 2로 먼저 걸러짐
- n이 소수인 경우, i가 n까지 커져야 되므로 while문에 등호가 들어감