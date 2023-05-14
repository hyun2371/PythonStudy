import sys

s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = map(int, sys.stdin.readline().split())
result = ''

while n != 0:
    result += str(s[n % b])
    n //= n

print(result[::-1])