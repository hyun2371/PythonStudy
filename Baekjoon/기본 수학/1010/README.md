### 문제

[https://www.acmicpc.net/problem/1010](https://www.acmicpc.net/problem/1010)

<br>

### 문제 요약

$nCr$

<br>

### 배운 점

math 라이브러리로 팩토리얼 값 구할 수 있음

<br>


```python
import math
import sys

t = int(input())
for _ in range(t):
    n, r = map(int, sys.stdin.readline().split())
    print(math.factorial(n) // (math.factorial(n-r) * math.factorial(r)))
```