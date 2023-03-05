# *****
# ****
# ***
# **
# *
# n= int(input())
# for i in range(0, n):
#     for j in range(n-i, 0, -1):
#         print("*", end="")
#     print()


# s*****
# s****
# ss***
# sss**
# ssss*

# n = int(input())
# for i in range(0, n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n - i, 0, -1):
#         print("*", end="")
#     print()


# ssss*ssss
# sss***sss
# ss*****ss
# s*******s
# *********    252


n = int(input())
for i in range(n):
    for j in range(0, n - i - 1):
        print(" ", end="")
    for j in range(0, 2 * i + 1):
        print("*", end="")
    print()
