

### 문제

[1065번: 한수](https://www.acmicpc.net/problem/1065)
<br><br>

### 문제 요약

한수: x의 각 자리가 등차 수열을 이루는 수

N이 주어졌을 때 N이하의 한수 개수 출력
<br><br>

### 슈도 코드

```
한자리수, 두자리수는 모두 한수
ex) N = 110 
		1~99

한 자리수 ~두자리수 (n<100)

	count = n

세자리수 (n≥100)

for i in range(100, n+1):

	i = str(i)

	if i[2]-i[1] = i[1] - i[0]:

		i는 한 수 → count+=1
```
<br><br>
### 제출 코드
```python
def get_count(n):
    count = 0
    if n < 100:
        return n
    for i in range(100, n + 1):
        i = str(i)
        if int(i[2])-int(i[1]) == int(i[1]) - int(i[0]):
            count += 1
    return count + 99

n = int(input())
print(get_count(n))
```
<br><br>
### 배운 점

다른 풀이

```python
for i in range (100, n+1)
    nums = list(map(int,str(i))

    if nums[2]-num[1] == nums[1]-nums[0]:
	    count+=1
```