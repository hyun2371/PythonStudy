### 문제

[4673번: 셀프 넘버](https://www.acmicpc.net/problem/4673)
<br><br>

### 문제 요약

10000보다 작거나 같은 셀프 넘버 출력

셀프넘버: 생성자가 없는 숫자

d(n) : n과 n의 각 자리수 더함

ex) d(33)

33 33+3+3 = 39 39+3+9=51 …

33은 39의 생성자, 39는 51의 생성자
<br><br>
### 슈도 코드

```
for k 1~10000:

	total =0

	for i in str(k):
		total +=int(i)
	total +=k

	리스트에서 total 제거

lst = 1~10000
lst 요소 출력
```
<br><br>
### 배운 점

lst.remove(i)인데, i가 lst에 없으면 오류 남

lst에 i가 있는지 먼저 확인하기