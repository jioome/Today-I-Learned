import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline  
k = int(input())

def dfs(start,group):
    visited[start] = group
    for i in graph[start]:
        if not visited[i]:
            a = dfs(i,-group)
            if not a : # 그룹값을 -1로 주어 dfs를 돈다.
                return False
        elif visited[i] == visited[start]: # 만약 현재 정점과 연결된 정점의 그룹값이 같다면
            return  False 
    return True 

for _ in range(k):
    v,e = map(int,input().split())
    graph = [[]for _ in range(v+1)]
    visited = [False] *(v+1)
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,v+1):
        if not visited[i] : 
            result = dfs(i,1) 
        if not result :
            break
    print("YES" if result else "NO")


