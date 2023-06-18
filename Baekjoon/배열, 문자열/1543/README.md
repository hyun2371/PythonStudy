### 문제

https://www.acmicpc.net/problem/1543

<br>

### 문제 요약

문자열에서 특정 단어가 중복 안되게 몇 번 나오는지

ex) ababababa → aba

총 2번

<br>

### 슈도 코드

```
문자열 s 입력받기
특정 단어 k입력 받기
result = 0  #단어 수

인덱스가 문자열 넘지 않도록 반복
if s[i+ len(k)] == k  #단어 포함
	result += 1
  인덱스 += k 길이

else  # 단어 포함 x
	인덱스 += 1
```