import sys
sys.setrecursionlimit(10000)

def dfs(x, y, graph):
    if x <= -1 or x >= w or y <= -1 or y >= h:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y, graph)
        dfs(x+1, y, graph)
        dfs(x, y-1, graph)
        dfs(x, y+1, graph)
        return True
    return False


t = int(sys.stdin.readline())
for _ in range(t):
    w, h, k = map(int, sys.stdin.readline().split())
    graph = [[0] * h for _ in range(w)]

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1

    result = 0
    for i in range(w):
        for j in range(h):
            if dfs(i,j, graph):
                result += 1
    print(result)