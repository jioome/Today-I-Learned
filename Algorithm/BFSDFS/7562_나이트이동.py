import sys 
from collections import deque
sys.stdin =open('in.txt','rt')
input = sys.stdin.readline 

t = int (input()) # 테스트 수 
dx = [-2, -2, 2, 2, -1, 1,-1, 1]
dy = [-1, 1,-1, 1, -2, -2, 2, 2]

for i in range(t):
    l = int(input())
    start_x,start_y = map(int,input().split())
    end_x,end_y = map(int,input().split())
    visited = [[0]*l for _ in range(l)]
    visited[start_x][start_y] = 1  # 방문 확인 
    queue = deque()
    queue.append((start_x,start_y,0)) # 이동 횟수까지 넣어준다. 

    while queue : 
        x,y,move = queue.popleft()
        if x == end_x and y == end_y : 
            print(move)
            break 
        for i in range(8):
            nx = x+ dx[i]
            ny = y + dy[i] 
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0 :
                visited[nx][ny] = 1 
                queue.append((nx,ny,move+1))

