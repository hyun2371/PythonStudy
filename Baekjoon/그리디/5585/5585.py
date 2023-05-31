cost = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
result = 0

for i in coins:
    if cost == 0:
        break
    result += cost // i
    cost = cost % i
print(result)