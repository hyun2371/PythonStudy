### 문제

[https://www.acmicpc.net/problem/1850](https://www.acmicpc.net/problem/1850)

<br>

### 문제 요약

1로만 이뤄진 A, B의 최대 공약수 구하기

입력

각각 A, B가 이루는 1개수

출력

A, B의 최대 공약수

<br>

### 슈도 코드

유클리드 호제법

A> B

A % B = R 

B와 R의 최대 공약수가 A와 B의 최대공약수이다.

```python
if a> b:
	swap(a,b)

print('1'*gcd(a,b))

def gcd(a,b):
	if a % b == 0:
		return b
	gcd(b, a % b)
```

### 배운점

swap (a,b)

`a, b = b, a`