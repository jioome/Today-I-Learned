# 상하좌우 중에 하나라도 그래프 범위에 벗어나 버리면 
# False 를 리턴하기 때문에 계속 False 를 return 하고 있음 

import sys

# input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀함수 깊이 제한 풀기
t = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def DFS(x,y):
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if xx < 0 or yy < 0 or xx >= n or yy >= m or graph[xx][yy] == 0:
            pass
            # pass 대신 return False 를 쓸 경우 
            # 상하좌우 중에 하나라도 그래프 범위에 벗어나 버리면 
            # False 를 리턴하기 때문에 계속 False 를 return 하고 있음 
        else : 
            graph[xx][yy] = 0  # 위치가 중요, 헷갈림
            DFS(xx,yy)


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    cnt = 0

    # 배추 심기
    for _ in range(k):
        r,c = map(int, input().split())
        graph[c][r] = 1  # 왜 [c][r] 임??

    # DFS
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                DFS(x,y)
                cnt+=1
    print(cnt)