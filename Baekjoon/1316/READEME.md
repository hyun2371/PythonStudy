### 문제

[1316번: 그룹 단어 체커](https://www.acmicpc.net/problem/1316)
<br><br>
### 문제 요약

조건에 맞는 문자 개수

각 문자가 연속해서 나타나야 함

단어 개수 n

ex) happy → o

abcabc →x
<br><br>
### 슈도 코드

a =[]

for i range (n):

s 입력 받기

for i in range(len(s))

if s[i] not in a

a.append(s[i])

elif (s[i-1] ≠s[i])) // s[i] in a + 연속아님 (이전에 나온적 있음, 연속 아님)

return false

return true
<br><br>
### 테스트 코드 작성 (한 문자열 판단)

```python
st = input()

def check(s):
    a = []
    for i in range(len(s)):
        if s[i] not in a:  # 기존에 나온 문자가 아님
            a.append(s[i])
        elif i > 0 and s[i - 1] != s[i]:  # 기존에 나온 문자 && 불연속
            return False
		print(a)
    return True

if check(st) is True:
    print(1)
else:
    print(0)
```