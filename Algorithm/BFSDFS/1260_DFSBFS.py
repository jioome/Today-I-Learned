import queue
import sys
from collections import deque
# DFS : 재귀 , 스택
# BFS : 큐 deque
def dfs(v):
    print(v,end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue : 
        n = queue.popleft()
        print(n,end = ' ')
        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


input = sys.stdin.readline
n,m,v = map(int,input().split())
graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()
dfs(v)
print()
visited = [False] *(n+1)
bfs(v)
