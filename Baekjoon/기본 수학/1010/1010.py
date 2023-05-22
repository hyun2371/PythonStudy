# import sys
#
# def fact(k):
#     if k <= 1:
#         return 1
#     return k * fact(k - 1)
#
# t = int(input())
# for _ in range(t):
#     r, n = map(int, sys.stdin.readline().split())
#     print(fact(n) // (fact(n-r) * fact(r)))



import math
import sys

t = int(input())
for _ in range(t):
    n, r = map(int, sys.stdin.readline().split())
    print(math.factorial(n) // (math.factorial(n-r) * math.factorial(r)))

