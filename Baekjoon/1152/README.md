### 문제

[1152번: 단어의 개수](https://www.acmicpc.net/problem/1152)
</br></br>

### 문제 요약

공백으로 이뤄진 문자열

문자열 단어 개수 세기

문자열은 공백으로 시작하거나 끝날 수 있음
</br></br>

### 배운 점

시작이나 끝에 공백 있을 수 있음→strip() 사용

strip(): 양쪽 공백 제거

lstrip(), rstrip(): 왼, 오 공백 제거
</br></br>

다른 풀이
```java
lst = list(input().split())
print(len(lst))
```