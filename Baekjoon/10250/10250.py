tries = int(input())
for i in range(tries):
    h, w, n = map(int, input().split())
    if n % h == 0:
        ans_h = str(h)
        ans_w = str(n // h)
    else:  # 나머지 있는 경우
        ans_h = str(n % h)
        ans_w = str(n // h + 1)
    if len(ans_w) == 1:
        ans_w = '0' + ans_w
    print(ans_h + ans_w)
