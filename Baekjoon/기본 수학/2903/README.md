### 문제

[https://www.acmicpc.net/problem/2903](https://www.acmicpc.net/problem/2903)

<br>

### 문제 요약

초기상태 - 정사각형 점 4개

각 변 중앙, 정사각형 중심에 점 추가

중복되는 점을 제외했을 때, n번을 거친 후 점을 몇 번 저장해야 하는지

<br>

### 문제 아이디어

![https://postfiles.pstatic.net/MjAyMzA1MTNfMTUy/MDAxNjgzOTU0MDQ3MTEx.2p7PhFtxa573gJLyL5LpXBPYS2auy1GR4veFdYPaWiQg.LF4kRV-b0vfJe80oQEuwApPeJ2M2VtImNy-6uzKrZwIg.PNG.loveanna1207/image.png?type=w773](https://postfiles.pstatic.net/MjAyMzA1MTNfMTUy/MDAxNjgzOTU0MDQ3MTEx.2p7PhFtxa573gJLyL5LpXBPYS2auy1GR4veFdYPaWiQg.LF4kRV-b0vfJe80oQEuwApPeJ2M2VtImNy-6uzKrZwIg.PNG.loveanna1207/image.png?type=w773)

1  &nbsp;&nbsp; (2+1) * (2+1)

2  &nbsp;&nbsp; (3+2) * (3+2) 

3  &nbsp;&nbsp; (5+4) * (5+4)

4  &nbsp;&nbsp; (9+8) * (9+8) 

5  &nbsp;&nbsp; (17+16) * (17+16) = 1089 

6  &nbsp;&nbsp; (33+32) * (33+ 32)

<br>

```
(k+(k-1)) * (k+(k-1))

k = 2^0+1
	  2^1+1
	  2^2+1
	  2^3+1
	  2^4+1
	  2^5+1
```