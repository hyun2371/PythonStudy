n, m = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
for i in range(0, n - 2):
    for j in range(1, n - 1):
        for k in range(2, n):
            if i == j or j == k or k == i:
                continue
            total = lst[i] + lst[j] + lst[k]
            if ans < total <= m:
                ans = total

print(ans)
