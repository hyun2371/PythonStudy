def check_p(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


startN = int(input())
endN = int(input())
p_lst = []

for num in range(startN, endN + 1):
    if check_p(num):
        p_lst.append(num)

if len(p_lst) == 0:
    print(-1)
else:
    print(sum(p_lst))
    print(p_lst[0])
