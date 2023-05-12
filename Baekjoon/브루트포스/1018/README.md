### 문제

[https://www.acmicpc.net/problem/1018](https://www.acmicpc.net/problem/1018)

<br>

### 문제 요약

8 X 8 체스판으로 잘라낸 후 몇 개의 정사각형을 다시 칠함

<br>

**입력**

체스판 n, m ( 8 < n, m ≤ 50 )

체스 색깔 n줄

<br>

**출력**

다시 칠하는 정사각형 최소 개수

<br>

### 문제 아이디어

체스판 넘어가지 않을 때까지 반복

행 1~ 8 번째 칸 .. n-7 ~ n 

열 1~ 8 번째 칸 .. n-7 ~ n

i) 첫 칸 검정

ii) 첫 칸 흰색

두 경우 모두 다 해보고 작은 개수 cnt 구하기

cnt 값들 중 최소값 구하기

```
list=[]
for a 1~ n-8
	for b 1 ~ n-8
		cnt1 = 0
		cnt2 = 0

		for i a ~ a+7
			for j b ~ b+7

				if (i+j) % 2 == 0
					if chess[i][j] != 'B'
						cnt1 +=1
					if chess[i][j] != 'W'
					
				else
					if chess[i][j] != 'W'
						cnt1 += 1
					if chess[i][j] != 'B'
						cnt2 +=1

		list.append(min(cnt1, cnt2))

min(list)
```