from collections import deque
import sys
sys.stdin =open('in.txt','rt')
m,n = map(int,input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int,input().split())))
queue = deque()

# queue에 처음에 받은 토마토의 위치 좌표를 append 시킨다
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i,j))


dx = [-1,0,1,0]
dy = [0,-1,0,1]
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if tomato[nx][ny] == -1:
                continue
            if tomato[nx][ny] == 0:
                queue.append((nx,ny))
                tomato[nx][ny] = tomato[x][y]+1 # 익히고 1을 더해주면서 횟수를 세어주기
                
if 0 in tomato : 
    print(-1)
else:
    print(max(map(max,tomato))-1) # 처음 토마토 시작을 1로 표현했으니 1을 빼준다