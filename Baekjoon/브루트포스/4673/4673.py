lst = [i for i in range(1, 10001)]


for k in range(1, 10001):
    total = 0 # 생성자로 만든 수
    for i in str(k):
        total += int(i)
    total += k
    if total in lst:
        lst.remove(total)


print(*lst, sep='\n')
