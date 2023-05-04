### 문제

[https://www.acmicpc.net/problem/10828](https://www.acmicpc.net/problem/10828)

<br>

### 슈도 코드

```
- push(x): x 삽입
    
    → list.append(x)
    
- pop(): 맨 위 삭제 및 출력
    
    → print(list.pop())
    
- size(): 개수
    
    → print(len(list))
    
- empty(): 비어있는지 여부
    
    → print(int(len(list)==1))
    
- top(): 맨 위 출력 (비어있으면 -1 출력)
    
    →print(list[list(len)-1])
```

<br>

### 배운점

한 줄 씩 입력 받아 공백으로 구분하기

`cmd = input().split()`