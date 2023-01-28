### 문제

[5622번: 다이얼](https://www.acmicpc.net/problem/5622)
</br></br>

### 문제 요약

숫자 1 → 2초

한 칸 옆에 있는 숫자 걸기 → 1초씩 더 걸림

번호 대신 문자로 주어짐

각 알파벳에 해당하는 숫자 걸기
</br></br>

**예시**

UNUCIC

868242

ABC→3초

WXYZ →10초


</br>
문자열 요소 - ord(A) = 0
</br></br></br>

### 슈도 코드

0 1 2 → 3초 n//3=0

3 4 5 n//3=1

6 7 8

9 10 11

12 13 14

15 16 17 18       5 5 5 6 n//3==5 or n = 18

19 20 21             6 6 7 n//3==6 or n = 21

22 23 24 25 

for 문자열 요소  in 문자열

n = ord(문자열 요소) - ord(’A’) 
</br></br>
### 제출 코드

```python
s = input()

t = 0
for i in s:
    n = ord(i) - ord('A')
    if n // 3 == 0:
        t += 3
    elif n // 3 == 1:
        t += 4
    elif n // 3 == 2:
        t += 5
    elif n // 3 == 3:
        t += 6
    elif n // 3 == 4:
        t += 7
    elif n // 3 == 5 or n == 18:
        t += 8
    elif n // 3 == 6 or n == 21:
        t += 9
    else:
        t += 10
print(t)
```
</br></br>
### 배운 점

- 다른 코드
    
    ```python
    word = input()
    dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    time = 0
    
    for i in range(len(word)):
        for d in dial:  # 다이얼 원소 하나씩 추출
            if word[i] in d:
                time += dial.index(d) + 3
    print(time)
    ```
    <br>

- 문자열에 특정 문자 있는지
    
    if ‘A’ in ‘ABC’
    
    print(”true”)
    
    →항상 true를 출력