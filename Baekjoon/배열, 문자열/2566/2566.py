a=[]
for i in range(9):
    a.append(list(map(int, input().split())))

max_v, max_i, max_j = 0, 0, 0

for i in range(9):
    for j in range(9):
        if a[i][j] > max_v:
            max_v = a[i][j]
            max_i = i
            max_j = j

print(max_v)
print(max_i+1, max_j+1)