### 문제

[2231번: 분해합](https://www.acmicpc.net/problem/2231)
<br><br>

### 문제 요약

N이 주어졌을 때 N의 가장 작은 생성자 구하기

245는 256의 생성자

245의 분해합은 256

2+4+5+245 = 256

생성자 없으면 0 출력
<br><br>

### 슈도 코드

```
n 입력 받기
ans = 0

k → 1~n
	k_str = str(k)
    
	total = 0

	for i 0~k_str.len-1

	 total += int(k_str[i])

	total+= k

	if total == n
		ans = k
		break

print(ans)
```

<br><br>

### 추가 테스트

1+3+4+5+1345 = 1358

1+1+1+0 +1110 = 1113
<br><br>

### 배운점

k의 각 자리 숫자를 더하기 → map 활용

```python
total = sum((map(int, str(k))))
```