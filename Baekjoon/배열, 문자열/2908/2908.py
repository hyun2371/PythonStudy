# n1, n2 = input().split()
#
# r_n1 = ""
# r_n2 = ""
# for i in range(2, -1, -1):
#     r_n1 += n1[i]
#     r_n2 += n2[i]
#
# print(max(int(r_n1), int(r_n2)))

n1, n2 = input().split()
r_n1 = int(n1[::-1])
r_n2 = int(n2[::-1])

print(max(r_n1, r_n2))