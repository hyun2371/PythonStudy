### 문제

[10809번: 알파벳 찾기](https://www.acmicpc.net/problem/10809)
</br></br>
### 문제 요약

단어가 포함되어 있는 경우 처음 등장하는 위치를

포함되지 않은 경우 -1 출력
</br></br>

### 슈도 코드

알파벳 리스트 lst -1로 초기화

s 입력 받기

for i in range(len(s)):

ind = s [i] - ‘a’ 알파벳 순서    0~25

if lst[ind] == -1   // 처음 등장

lst[ind] = i
</br></br></br>

### 배운 점

다른 풀이

```python
s = input()
lst = list(range(ord('a'), ord('z')+1))

for i in lst:
    print(s.find(chr(i)), end = " ")
```

find(’a’): a의 인덱스 반환, 없으면 -1
</br></br></br>

오류

unsupported operand type(s) for -: 'str' and 'str’ 

```python
ind = ord(s[i]) - ord('a')
```

해결
```python
ind = ord(s[i]) - ord('a')
```