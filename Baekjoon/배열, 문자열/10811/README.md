### 문제

[10811번: 바구니 뒤집기](https://www.acmicpc.net/problem/10811)
<br><br>
### 문제 요약

N개 바구니 1~N 번호 순서대로

역순으로 만들 범위를 정하고, 그 범위 내 바구니 순서를 역순으로 

왼쪽 바구니부터 출력

입력

N개  바꾸는케이스수M

범위시작(i) 끝(j)
<br><br>

### 슈도 코드

예시

5 4 //1 2 3 4 5

1 2 //2 1 3 4 5

3 4 // 2 1 4 3 5

1 4 // 3 4 1 2 5

2 2 // 3 4 1 2 5

```
n만큼 배열 초기화
M만큼 반복
	/*tmp[] =a[1]~a[4] reverse
	a[]=tmp[]*/

	cnt=0
	for ind in range(j,i-1,-1)
		tmp[cnt] = a[ind-1]
		cnt++
		
```
<br><br>
### 제출 코드

```python
n, m = map(int, input().split())
a = [i + 1 for i in range(n)]  # 바구니 초기화
tmp = []  # 역순 담기

for _ in range(m):
    i, j = map(int, input().split())

    for ind in range(j, i - 1, -1):  # 역순
        tmp.append(a[ind - 1])  # 인덱스는 0부터 시작

    cnt = 0 # tmp의 인덱스
    for ind in range(i, j + 1):
        a[ind - 1] = tmp[cnt]
        cnt += 1
    tmp = []

print(*a, end=" ")
```
<br><br>
### 배운점

다른 풀이

```python
n, m = map(int, input().split())
a = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    a = a[:i-1] + a[i-1:j][::-1] + a[j:]

print(*a, end=" ")
```