### 문제

[1712번: 손익분기점](https://www.acmicpc.net/problem/1712)
<br><br>

### 문제 요약

A: 고정비용

B: 가변 비용

C: 한 대당 판매비용
<br><br>

### 슈도 코드

B≥C → print(-1)

A+B*n > C*n

(B-C) n > -A

n> A/(C-B)
<br><br>

### 제출 코드

```python
import sys

a, b, c = map(int, sys.stdin.readline().split())

if b >= c:
    print(-1)
else:
    print(a // (c - b) + 1)
```
<br><br>
### 배운 점

A+B*n > C* n으로 놓고

n을 1씩 증가시키면 시간초과

->n을 바로 구해야 함