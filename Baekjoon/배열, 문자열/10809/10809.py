lst = [-1] * 26
s = input()
for i in range(len(s)):
    ind = ord(s[i]) - ord('a')
    if lst[ind] == -1:
        lst[ind] = i
print(*lst)


