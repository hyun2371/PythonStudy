### 문제

[2292번: 벌집](https://www.acmicpc.net/problem/2292)
<br><br>
### 문제 요약

1에서 N번 방까지 최소 몇 개의 방 지나가는지 계산



<img src="https://postfiles.pstatic.net/MjAyMzAyMThfNTEg/MDAxNjc2NzI5NTI1NDU5.E-CSXkuXXimHmqKw_kvkDjk3XpwWtlk34QptujjWzdAg.E_90EtfRbG8GnytK8F9B4vIbH3G2yc1VHusF4LonP3og.PNG.loveanna1207/image.png?type=w773" width="400" height="400"/>
<br><br>

### 슈도 코드

1→0

2~7→1    ~ 1+6

8~19→2     ~ 1+6+12

20~37→3   ~ 1+6+12+18

38~61→4  ~ 1+6+12+18+24  

1+6+12+18+24
<br><br><br>

cmp=1.    n= 61

n > cmp

cmp = cmp + 6*1(cnt)  //cmp = 7

n> cmp

cmp = cmp + 6*2(cnt) // cmp = 19

n> cmp

cmp = cmp + 6*3(cnt) //cmp = 37

n> cmp

cmp = cmp + 6*4(cnt) // cmp = 61
<br><br>

cnt + 1 출력
<br><br><br><br>
```
cmp=1 cnt =0 n = 61

while (True)
	if (n≤cmp)
		break

	cnt ++
	cmp += 6* cnt

print(cnt+1)
```
<br><br>
### 제출 코드

```python
n = int(input())
cnt = 0
cmp = 1

while True:
    if n <= cmp:
        break
    cnt += 1
    cmp += 6 * cnt

print(cnt + 1)
```