n, m = map(int, input().split())
a = [i + 1 for i in range(n)]  # 바구니 초기화
tmp = []  # 역순 담기

for _ in range(m):
    i, j = map(int, input().split())

    for ind in range(j, i - 1, -1):  # 역순
        tmp.append(a[ind - 1])  # 인덱스는 0부터 시작

    cnt = 0 # tmp의 인덱스
    for ind in range(i, j + 1):
        a[ind - 1] = tmp[cnt]
        cnt += 1
    tmp = []

print(*a, end=" ")

