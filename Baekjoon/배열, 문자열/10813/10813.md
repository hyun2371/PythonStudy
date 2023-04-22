### 문제

[https://www.acmicpc.net/problem/10813](https://www.acmicpc.net/problem/10813)

<br>

### 문제 요약

바구니에 1~n 번호 매겨져 있음

바구니 두 개 선택해 안의 공을 교환

5 4  공 수 바꿀 수

1 2 → 2 1 3 4 5

3 4 → 2 1 4 3 5

1 4 → 3 1 4 2 5

2 2 → 3 1 4 2 5

<br>


### 슈도 코드

```
n, m 입력 받기
리스트 1~n으로 초기화

4번 반복
	i, j 입력 받기
	list[i-1] = tmp
	list[i-1] = list[j-1]
	list[j-1] = tmp

list 출력
```