### 문제

[11047번: 동전 0](https://www.acmicpc.net/problem/11047)

<br>

### 문제 요약

동전을 N 종류 가지고 있다

동전을 사용해 가치의 합을 k로 만들려고 함

k를 만드는 동선 개수의 최대값을 구하자

<br>

### 슈도 코드

```
각 줄에 들어오는 코인 입력 받기

n번 반복

	coins.append(int(input())

K가 0일 때까지 반복

	if k < coins[i] → continue
	count += K / coins[i]
	K = K % coins[i]
```

<br>

### 문제 아이디어

가장 큰 단위의 동전 먼저 거슬러 준다.

동전의 큰 단위가 항상 작은 단위의 배수이므로

작은 단위의 동전들을 종합해 다른 해가 나올 수 없다.

그리디 알고리즘 적용 불가능한 경우

ex) 500,400,100 으로 800원 만들기

500+100+100+100 →3

400+400 → 2 

<br>

### 다른 풀이

```python
for i in range(n-1,-1,-1):
    if k < coins[i]:
        continue
    count += k // coins[i]
    k = k % coins[i]
```

while이 아닌 for로 풀면 ind값을 처리해주지 않아도 됨