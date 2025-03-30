import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    for nxt in graph[x]:
        if depth[nxt] == -1:
            parent[nxt][0] = x
            depth[nxt] = depth[x] + 1
            dfs(nxt)

n = int(input())

parent = [[-1] * 20 for _ in range(n)] 
depth = [-1] * n
graph = [[] for _ in range(n)]  

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

depth[0] = 0
dfs(0)

for i in range(19):
    for j in range(n):
        if parent[j][i] != -1:
            parent[j][i + 1] = parent[parent[j][i]][i]

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
    for i in range(19, -1, -1):
        if diff & (1 << i):
            a = parent[a][i]
    if a != b:
        for i in range(19, -1, -1):
            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]
        a = parent[a][0]

    print(a + 1)
