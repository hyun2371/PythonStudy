c = int(input())

for i in range(c):
    lst = list(map(int, input().split()))
    lst_len = lst.pop(0) # 리스트 길이 추출

    avg = sum(lst) / lst_len
    cnt = 0

    for j in lst:
        if j > avg:
            cnt += 1
    result = cnt / lst_len * 100
    print("%0.3f%s" % (result, "%"))
