### 문제

[1436번: 영화감독 숌](https://www.acmicpc.net/problem/1436)
<br><br>
### 문제 요약

666이 들어간 수 N번째 구하기

ex) 666 1666 2666 …
<br><br>
### 슈도 코드

```
while(){

	if str이  666 포함
		count++

	if (count == N)
		break

	ans++
}

print(ans)
```
<br><br>
### 제출 코드

```python
import sys
n = int(sys.stdin.readline())

ans = 0
cnt = 0
while True:
    if "666" in str(ans):
        cnt += 1
    if cnt == n:
        break
    ans += 1

print(ans)
```
<br><br>
### 배운 점

sys.stdin.readline()에서 int() 있어야 함