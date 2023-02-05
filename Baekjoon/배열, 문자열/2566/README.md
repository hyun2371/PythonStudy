### 문제

[2566번: 최댓값](https://www.acmicpc.net/problem/2566)
<br><br>
### 문제 요약

9x9 행렬의 최대값 구하여 위치와 함께 출력

최대값이 중복일 경우 한 곳의 위치만 출력
<br><br>
### 제출코드

```python
a=[]
for i in range(9):
    a.append(list(map(int, input().split())))

max_v, max_i, max_j = 0, 0, 0

for i in range(9):
    for j in range(9):
        if a[i][j] > max_v:
            max_v = a[i][j]
            max_i = i
            max_j = j

print(max_v)
print(max_i+1, max_j+1)
```
<br><br>
### 배운 점

다른 풀이

```python
max_v, max_i, max_j = 0, 0, 0

for i in range(9):
    a = list(map(int, input().split()))
    print(a)
    if max(a) > max_v:  # 한 행 최대값과 비교
        max_v= max(a)
        max_i = i
        max_j = a.index(max_v)
        print(max_j)

print(max_v)
print(max_i + 1, max_j + 1)
```