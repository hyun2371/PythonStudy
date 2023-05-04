### 문제

[https://www.acmicpc.net/problem/10812](https://www.acmicpc.net/problem/10812)

<br>

### 문제 요약

N개 바구니

M번 바구니의 순서를 회전

바구니 범위 begin~end

기준이 되는 바구니 mid

begin .. mid .. end 순서를

mid mid+1 .. end-1 end begin begin+1 .. mid-1로 바꿈

<br>

예제

```
10 5
1 6 4
3 9 8
2 10 5
1 3 3
2 6 2
```

**1 2 3 4 5 6**   7 8 9 10 

(1) 4 5 **6 1 2 3 7 8 9** 10 

(2) 4 **5 8 9 6 1 2 3 7 10**

(3) **4 6 1** 2 3 7 10 5 8 9

(4) 1 **4 6 2 3 7** 10 5 8 9

(5) 1 **4 6 2 3 7** 10 5 8 9

<br>

### 슈도 코드

```
result = [1 .. 10]

for _ in range(5)
	tmp[i~j] = result[k]~ result[j]   + result[i] ~ result[j-1]
	result[i~j] = tmp [i~j]

print(*result)
```
<br>

### 다른 풀이

```python
import sys

n, m = map(int, sys.stdin.readline().split())
result = [i + 1 for i in range(n)]

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    i, j, k = i-1, j-1, k-1

    tmp = result[k:j+1] + result[i:k]
    result = result[:i] + tmp + result[j+1:]

print(*result)
```