import sys

def is_vps(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) == 0 or stack[len(stack) - 1] != '(':
                return "no"
            stack.pop()
        elif s[i] == ']':
            if len(stack) == 0 or stack[len(stack) - 1] != '[':
                return "no"
            stack.pop()

    if len(stack) == 0:
        return "yes"
    else:
        return "no"


while True:
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break
    print(is_vps(s))
