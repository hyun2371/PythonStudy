### 문제

[3009번: 네 번째 점](https://www.acmicpc.net/problem/3009)
<br><br>

### 문제 요약

세 점이 주어졌을 때 직사각형 만들기 위해 필요한 네 번째 점 좌표 출력
<br><br>
### 슈도 코드

```
x1, y1 입력 받기
x2, y2 
x3, y3

30 20 
10 10
10 20

x에 추가

for i in x_lst:

	x_list.count(i)

	count값 1 → x4= i

y도 반복
```
<br><br>
### 배운점

코드 간결화

```python
x1, y1 = input().split()
x2, y2 = input().split()
x3, y3 = input().split()

x_lst = []
x_lst.append(x1)
x_lst.append(x2)
x_lst.append(x3)

y_lst = []
y_lst.append(y1)
y_lst.append(y2)
y_lst.append(y3)

##############
for i in range(3):
    x, y = input().split()
    x_lst.append(x)
    y_lst.append(y)
```