import sys

n = int(sys.stdin.readline())
result = []
graph = []
ind = 0

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
cnt = 0

def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return cnt
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        cnt+= 1 # 단지별 집 수 저장
        return cnt
    return cnt


for i in range(n):
    for j in range(n):
        c = dfs(i,j)
        if c>0:
            result.append(c)
            cnt =0

print(len(result))
result.sort()
print(*result, sep="\n")