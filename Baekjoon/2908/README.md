### 문제

[2908번: 상수](https://www.acmicpc.net/problem/2908)
</br></br>

### 문제 요약

세자리수 2개 입력 받음

뒤집어서 큰 수 출력
</br></br>

### 제출 코드

```java
n1, n2 = input().split()

r_n1 = ""
r_n2 = ""
for i in range(2, -1, -1):
    r_n1 += n1[i]
    r_n2 += n2[i]

print(max(int(r_n1), int(r_n2)))
```
</br></br>
### 배운 점

다른 풀이

```java
n1, n2 = input().split()
r_n1 = int(n1[::-1])
r_n2 = int(n2[::-1])

print(max(r_n1, r_n2))
```

문자열 역순으로 출력 -> a[::-1]