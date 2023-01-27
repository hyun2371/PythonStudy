
n = int(input())
lst = list(map(int, input().split()))

maxN = lst[0]
for i in range(n):
    if lst[i] > maxN:
        maxN = lst[i]

result = 0
for i in lst:
    result += i/maxN * 100

print(result/len(lst))



