n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

count = 0
ind = n - 1

while k != 0:
    if k < coins[ind]:
        ind -= 1
        continue

    count += k // coins[ind]
    k = k % coins[ind]
    ind -= 1