
# 한 자리 수 -> 앞에 0 붙임
def trans_double(num):
    if len(num) == 1:
        num = "0" + num
    return num


x = trans_double(input())
result = x

n = 0

while True:
    n += 1
    # ab
    a = result[0]
    b = result[1]

    result = b + str((int(a) + int(b)) % 10)
    result = trans_double(result)

    if result == x:
        break

print(n)
