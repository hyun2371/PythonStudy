import sys
n, m = map(int, sys.stdin.readline().split())
result = [i+1 for i in range(n)]
tmp = [i+1 for i in range(n)]


for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    i, j, k = i-1, j-1, k-1

    tmp_ind = i # 바꿀 시작 위치

    for ind in range(k, j + 1):
        tmp[tmp_ind] = result[ind]
        tmp_ind += 1

    # i~ k-1
    for ind in range(i, k):
        tmp[tmp_ind] = result[ind]
        tmp_ind += 1

    # 바꾼 바구니 영역을 result에 대입
    for ind in range(i, j + 1):
        result[ind] = tmp[ind]

print(*result)