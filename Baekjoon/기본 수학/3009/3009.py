x_lst = []
y_lst = []

for i in range(3):
    x, y = input().split()
    x_lst.append(x)
    y_lst.append(y)

for i in x_lst:
    if x_lst.count(i) == 1:
        x4 = i
        break

for i in y_lst:
    if y_lst.count(i) == 1:
        y4 = i
        break

print(x4, y4)
