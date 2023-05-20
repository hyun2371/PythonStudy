## 삽입 정렬

- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
- 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작함

<br>

### 예시

![Untitled](https://postfiles.pstatic.net/MjAyMzA1MjBfMjA0/MDAxNjg0NTY4NTgzOTI4.leP9V852BIccul6i7ozebxcVcWL7LNYUSkD1OmMGkHYg.BgjndORS8BwmjdCJ6Bdw3_f_X3Hp_AT-wwqbwo0ma8Ug.PNG.loveanna1207/image.png?type=w773)

![Untitled](https://postfiles.pstatic.net/MjAyMzA1MjBfMjIz/MDAxNjg0NTY4NTk1MzA1.YdvLj6cnP2PasGvCnX92y23py7GeyE67ssw_QwxDT98g.wj6UIUFN6DQr88uYnE1v0DkTWoSvVRrmH7KbK-mZ79Ig.PNG.loveanna1207/image.png?type=w773)

![Untitled](https://postfiles.pstatic.net/MjAyMzA1MjBfMjUg/MDAxNjg0NTY4NjE1NzE2.UWZ-gbOsVRA9yN99lsLhgJtfprxUD1YNGCuXpbsVNUsg.Rih-GR_lDOXFXQN7_raMP-7-jQlY_Jw_OiKjITph2fIg.PNG.loveanna1207/image.png?type=w773)

![Untitled](https://postfiles.pstatic.net/MjAyMzA1MjBfMTA1/MDAxNjg0NTY4NjU1OTgx.czqH1wXRJ8klXkP9mCAo66MiBvAa3OL0sehBjp2R32Ug.k_ApBpSg1nNbpioIrnz6Ou7FsvNavUdIL1hE7HOPmQwg.PNG.loveanna1207/image.png?type=w773)

<br>
<br>

### 구현 코드

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
	for j in range(i, 0, -1): # 인덱스 i~1까지 1씩 감소하며 반복하는 문법
		if array[j] < array[j-1]: 
			array[j], array[j - 1] = array[j-1], array[j] #swap
		else: # 자기보다 작은 데이터 만나면 그 위치에서 멈춤
			break

print(array)
```
<br>
<br>

### 테스트

```
7 5 9 0

i = 1
for j in range(1, 0, -1)
	j = 1
	array[1] < array[0]
		array[1], array[0] swap

5 7 9 0

i = 2
for j in range(2, 0, -1)
	j = 2
	array[2] > array[1]
		break

5 7 9 0

i = 3
for j in range(3, 0, -1)
	j = 3
	array[3] < array[2]
		array[3], array[2] swap // 5 7 0 9

	j = 2
		array[2] < array[1]
			array[2], array[1] swap // 5 0 7 9

	j = 1
		array[1] < array[0]
			array[1], array[0] swap // 0 5 7 9
```

<br>
<br>
이미지 출처

[https://www.youtube.com/watch?v=KGyK-pNvWos&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=4&t=300s&ab_channel=동빈나](https://www.youtube.com/watch?v=KGyK-pNvWos&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=4&t=300s&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98)