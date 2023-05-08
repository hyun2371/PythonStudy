import sys

def dfs(v):
    visited[v] = 1

    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)
            result.append(i)


n = int(input())
m = int(input())
result = []
visited = [0] * (n+1)
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1

dfs(1)
print(visited.count(1)-1)