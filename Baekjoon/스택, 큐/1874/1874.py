import sys
cnt = 0  # 스택에 몇까지 push 됐는지
n = int(input())
stack = []

result = ""
for _ in range(n):
    k = int(sys.stdin.readline())  # 수열의 각 수 입력 받기
    if k > cnt:
        for i in range(cnt, k):
            stack.append(i+1)
            result += '+\n'
            cnt += 1
        stack.pop()
        result += '-\n'

    else:
        if stack[len(stack) - 1] != k:  # peek() != k
            result = "NO"
            break
        stack.pop()
        result += '-\n'

print(result)