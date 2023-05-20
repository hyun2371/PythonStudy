### 문제

[https://www.acmicpc.net/problem/2750](https://www.acmicpc.net/problem/2750)

<br>

### 선택 정렬

처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꿈

<br>

### 예시

<img src="https://postfiles.pstatic.net/MjAyMzA1MTlfMTEy/MDAxNjg0NTAwNjEwOTcy.GQcePh5f9GRp8_GEtAnEV4Oy86_QtKckgxeXqpP60x4g.veaqMBQ9-F1mKJFAAvwOCShvR333q-BwkVhjfi-j71Mg.PNG.loveanna1207/image.png?type=w773" width="400">

<br>

<img src="https://postfiles.pstatic.net/MjAyMzA1MTlfNzYg/MDAxNjg0NTAwNjE4MzM2.OezeRv8rViobgkJMVajs2R5cra5c9WHuzW0OnuIUjTEg.lb7My2iNfgtHAqiA52jTLCAz0nOH9-DG7RXWBPObGmog.PNG.loveanna1207/image.png?type=w773" width="400">

<br>

<img src="https://postfiles.pstatic.net/MjAyMzA1MTlfODgg/MDAxNjg0NTAwNjI4NjU2.jiOorbMnhZrXcetVvbkBEqHZax3MQGcjNkW-th6D1EIg.96BogEsZUJQ7F9M13NSTK8JipuMcfQGEaX3zJtopcTUg.PNG.loveanna1207/image.png?type=w773" width="400">

<br>

<img src="https://postfiles.pstatic.net/MjAyMzA1MTlfMTc1/MDAxNjg0NTAwNjM2NTcw.sTCK8vx4-Nwyrpt05ElUDNqN7HGLCJXhjFZbaMJmATEg.sSJ1rTGNshTU8v3KFLuJ_qmMTeRq_cWmIIAP4Kp-KYgg.PNG.loveanna1207/image.png?type=w773" width="400">

<br>
마지막은 원소가 하나 남으므로 위의 과정 생략 가능
<img src="https://postfiles.pstatic.net/MjAyMzA1MTlfODkg/MDAxNjg0NTAwNjQzNTc2.JmmU0o-r74C26VYrVtuUOc_g10-7t_MZDlbPTOUzGKIg.TNnePMJaxlJtx7APnNV74ElkrmwSnbDzkQppHbE7QLYg.PNG.loveanna1207/image.png?type=w773" width="400">

<br>
이미지 출처: https://www.youtube.com/watch?v=KGyK-pNvWos&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98 

<br>

### 테스트

```
7 5 9 0

i = 0
min_index = 0

	for j in range(1, 4)
		j = 1
		array[0] > array[1]:
			min_index = 1

		j = 2
		array[1] < array[2]:
			min_index = 1
	
		j = 3
		array[1] > array[3]:
			min_index = 3

	array[0], array[3] 바꾸기

0 *5 9 7*

i = 1
min_index = 1

	for j in range(2, 4)
		j = 2
		array[1] < array[2]
			min_index = 1
		
		j = 3
		array[1] <array[3]
			min_index = 1

	array[1], array[1] 바꾸기 → 그대로

0 5 *9 7*

i = 2
min_index = 2

for j in range(3,4)
	j = 3
	array[2] > array[3]
		min_index = 3

array[2], array[3] 바꾸기 

0 5 7 9
```