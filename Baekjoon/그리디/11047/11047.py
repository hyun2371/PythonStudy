n, k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

result = 0
for c in range(len(coins)-1,-1,-1):
    result += k // coins[c]
    k = k % coins[c]
print(result)
