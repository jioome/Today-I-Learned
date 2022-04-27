import sys,copy
sys.stdin =open('in.txt','rt')
input = sys.stdin.readline 
n = int(input())
graph = [] 

for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0 <= ny < n and check[nx][ny] > h:
            check[nx][ny] = 0 
            dfs(nx,ny,h)




## 최대 높이 
height = 0 
for i in graph:
    height = max(height,max(i))

#안전한 영역 최대 개수 

ans = []
for h in range(height):
    check = copy.deepcopy(graph)
    cnt = 0 
    for i in range(n):
        for j in range(n):
            if check[i][j] > h : 
                cnt += 1 
                check[i][j] = 0 
                dfs(i,j,h)
    ans.append(cnt)

print(max(ans))

    
