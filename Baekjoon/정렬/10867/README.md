## 퀵 정렬

- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘
- 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(pivot)으로 설정

<br>

### 예시
![Untitled](https://postfiles.pstatic.net/MjAyMzA1MjJfMTA2/MDAxNjg0NjgyMjg5NDQw.JeeVhA9Md3C4W7kEbLm_kVoI8pnv4DE56QBzWcfyRcEg.KAxCxY4UUuCfWdmK0O3_weAhTLj7a5SFnq4ADnVdfLwg.PNG.loveanna1207/image.png?type=w773)

<br>

![Untitled](https://postfiles.pstatic.net/MjAyMzA1MjJfMjMx/MDAxNjg0NjgyMjk4Nzkx.pjZbgXenxrl3pthjIbIsxGFMPULxCRhRLe6yUkig0xMg.DNkjnO6foYgdwSiVW8SGs8_SrnlJT_3q70KnM2QiaEcg.PNG.loveanna1207/image.png?type=w773)

<br>

![Untitled](https://postfiles.pstatic.net/MjAyMzA1MjJfMTk1/MDAxNjg0NjgyMzExNTM4.MstinC4-REVYtl3vzQB1g6yXJUZoQrNeEiY-cM4mzC0g.jYJFrt2h30xN6zKQ33JB32ThdvN2lMIxw2BCmy0wPkUg.PNG.loveanna1207/image.png?type=w773)

<br>

![Untitled](https://postfiles.pstatic.net/MjAyMzA1MjJfMTA2/MDAxNjg0NjgyMzIxMDU0.4rMkFMGyFVagLFuGt48Cx6dSvpEWbPIdLrQqI3E1pDgg.ZkLuylQUeeHdhWdU2RaxkU-WAEEwn4VfwiE9SBtRS5Eg.PNG.loveanna1207/image.png?type=w773)

<br>

![Untitled](https://postfiles.pstatic.net/MjAyMzA1MjJfMjIw/MDAxNjg0NjgyMzI2MjQ3.8tMdXvsReLR5bmze95uN9ffTzHoc3w5C7Rbrf80vx4wg.nZXEJqgcz3L2ZDzFFtaeZeAGOi32zmFmHqbMYfyDaoIg.PNG.loveanna1207/image.png?type=w773)

<br>

![Untitled](https://postfiles.pstatic.net/MjAyMzA1MjJfMTEy/MDAxNjg0NjgyMzM0Njg1.4e5BMKgTw3FQqhmCt9eAGwGZ-8EYJ4YSqdmfqNNbGWcg.xbX9u0E7wz9zS57RFwXEIMgi103U3jF7uJb37fx8qRog.PNG.loveanna1207/image.png?type=w773)



<br>

### 구현 코드

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
	if start >= end: #원소가 1개인 경우 종료
		return

	# 인덱스 값
	pivot = start # 피벗은 첫 번째 원소
	left = start + 1
	right = end

	while (left <= right): # 인덱스 교차되지 않을 때까지
		# 피벗보다 큰 데이터를 찾을 때까지 반복
		while(left <= end and array[left] <= array[pivot]):
			left += 1 # 오른쪽으로 이동
		
		# 피벗보다 작은 데이터 찾을 때까지 반복
		while(right > start and array[right] >= array[pivot]):
			right -= 1 # 왼쪽으로 이동

		if (left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
			array[right], array[pivot] = array[pivot], array[right]
		else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
			array[left], array[right] = array[right], array[left]
	
	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
	quick_sort(array, start, right - 1)
	quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1 )
print(array)
```

<br>
<br>


파이썬은 간략화 가능

```python
array = [5, 7, 9, 0, 3, 1, 6, 4, 8]

def quick_sort(array):
	if len(array) <= 1:
		return array
	pivot = array[0]
	tail = array[1:]

	left_side = [x for x in tail if x <= pivot] # 반복문에 들어온 x를 append
	right_side = [x for x in tail if x > pivot]

	return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```

출처

[https://www.youtube.com/watch?v=KGyK-pNvWos&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=4&t=300s&ab_channel=동빈나](https://www.youtube.com/watch?v=KGyK-pNvWos&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=4&t=300s&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98)

---

<br>


### 문제

[https://www.acmicpc.net/problem/10867](https://www.acmicpc.net/problem/10867)

<br>

### 배운 점

- 중복 제거
    
    set(list(array))
    
- 런타임 에러 (RecursionError)
    
    python이 정한 최대 재귀 깊이 변경
    
    sys.setrecursionlimit(10**6)