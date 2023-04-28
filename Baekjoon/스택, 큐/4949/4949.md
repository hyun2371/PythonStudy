### 문제

[https://www.acmicpc.net/problem/4949](https://www.acmicpc.net/problem/4949)

### 문제 요약

괄호 종류: ()와 [] 

‘(’, ‘)’  - ‘[’ ,‘]’  서로 짝을 이루며 차례로 와야 함

### 슈도 코드

(→ 0 입력

[ → 1입력 

) → 0 있는지 확인

pop()

] → 1 있는지 확인

pop()

```
while (s!= ".")
	s = input()
	is_vps(s)

def is_vps(s)

for i in range(len(s))
	s[i] == '(' or ']'
		stack.append(s[i])

	s [i] == ')'
		len(stack)!=0 or stack[len(stack)-1]!= '('
			return "no"
		stack.pop()

	s [i] == ']'
		len(stack)!=0 or stack[len(stack)-1]!= ']'
			return "no"
		stack.pop()

if (!stack.isEmpty())
	return "no"
else
	return "yes"
```