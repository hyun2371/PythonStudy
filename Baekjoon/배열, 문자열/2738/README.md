### 문제

[2738번: 행렬 덧셈](https://www.acmicpc.net/problem/2738)
<br><br>

### 문제 요약

n행 m열 행렬 덧셈
<br><br>

### 배운 점

다른 풀이

```python
n, m = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(a[i][j]+b[i][j], end=" ")
    print()
```