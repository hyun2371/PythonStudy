def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x ** (1 / 2)) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for _ in range(n):
    if is_prime(lst.pop(0)):
        cnt += 1
print(cnt)
