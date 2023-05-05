import sys

result = [[-1 for col in range(15)] for row in range(5)]

for r in range(5):
    line = sys.stdin.readline().rstrip()
    for c in range(len(line)):
        result[r][c] = line[c]

for c in range(15):
    for r in range(5):
        if result[r][c] == -1:
            continue
        print(result[r][c],end="")