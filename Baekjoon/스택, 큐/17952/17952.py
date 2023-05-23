import sys
n = int(sys.stdin.readline())
stack = []
result = 0
for _ in range(n):
    task = list(map(int, sys.stdin.readline().split()))
    if task[0] == 1:
        stack.append((task[1],task[2]))

    if len(stack)!=0:
        score, time = stack.pop()
        time -= 1
        if time == 0:
            result += score
        else:
            stack.append((score,time))


print(result)