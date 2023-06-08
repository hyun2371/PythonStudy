import sys
n = int(input())
cnt_lst = []
for _ in range(n):
    cnt_lst.append(int(sys.stdin.readline()))

result = 0
cnt_lst.reverse()
while not (max(cnt_lst) == cnt_lst[-1] and cnt_lst.count(max(cnt_lst))==1):
    max_ind = cnt_lst.index(max(cnt_lst))
    cnt_lst[max_ind] -= 1
    cnt_lst[-1] += 1
    result += 1

print(result)