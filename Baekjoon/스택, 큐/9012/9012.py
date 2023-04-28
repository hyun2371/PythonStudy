import sys


def is_vps(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(0)
        else:
            if len(stack) == 0:
                return "NO"
            stack.pop()
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


n = int(sys.stdin.readline())
for _ in range(n):
    ps = input()
    print(is_vps(ps))
