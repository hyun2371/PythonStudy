n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

min_p = price[0]
result = price[0] * length[0]

for i in range(1, n - 1):
    if price[i] < min_p:
        min_p = price[i]
    result += length[i] * min_p

print(result)