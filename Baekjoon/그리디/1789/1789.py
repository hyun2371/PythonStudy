
w_list = list(input().split())
s=[]

for i in range(len(w_list)):
    word = w_list[i]
    for char in word:
        if char == '<':
            while char !='>':
                s.append()
        s.append(char)
    for _ in range(len(s)):
        print(s.pop(),end="")
    print(" ",end="")
