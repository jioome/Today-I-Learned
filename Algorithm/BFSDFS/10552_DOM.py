import sys
sys.stdin =open('in.txt','rt')
input = sys.stdin.readline 
sys.setrecursionlimit(1000000)

n,m,p = map(int,input().split())
graph = [[]for _ in range(m+1)]
visited = [0]*(m+1)

for _ in range(n):
    a,b = map(int,input().split())
    graph[b].append(a) # 싫어하는 채널을 기준으로 graph를 만들어 준다

def dfs(start):
    global cnt 
    if visited[start] == 1: # 이미 방문한 경우 또 방문하면 사이클 생김 
        print(-1)
        return
    visited[start] = 1 

    if len(graph[start]) == 0 : # 채널을 바꿀 필요가 없을 때 / 채널 싫어하는 사람 없을 때
        print(cnt)
        return
    else : 
        next = graph[start][0] # 다음 채널로 바꿀 때 
        cnt +=1
        dfs(next)

    

cnt = 0 
dfs(p) 