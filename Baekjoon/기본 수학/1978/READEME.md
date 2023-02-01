### 문제

[1978번: 소수 찾기](https://www.acmicpc.net/problem/1978)
<br><br>
### 문제 요약

주어진 수들 중 소수 개수 출력
<br><br>
### 배운 점

for i in range(0,n)

if (n%i==0):

return false

에서 1~n-1 검증 결과는  1~루트(n) 검증과 동일
<br>

**예시**

1 2 3 4 | 6 8 12 24

int(루트 24)= 4

1~4 까지만 검증하면 됨

(1,24) (2,12) (3,8) (4,6) 이렇게 쌍을 이루므로
<br><br>
### 참고

[https://www.youtube.com/watch?v=LD-Px5YCd8Y](https://www.youtube.com/watch?v=LD-Px5YCd8Y)