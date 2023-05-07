import sys

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


a, b = map(int, sys.stdin.readline().split())

if b > a:
    a, b = b, a

print('1'*gcd(a, b))