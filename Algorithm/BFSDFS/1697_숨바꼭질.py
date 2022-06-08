from collections import deque
import sys

sys.stdin =open('in.txt','rt')
input = sys.stdin.readline 
n,k = map(int,input().split())
visited= [0]*(100001)

def bfs():
    q= deque()
    q.append(n)
    visited[n]= 1 
    while q : 
        x = q.popleft()
        dx = [-1,1,x]

        for i in range(3):
            nx = x + dx[i]
            if 0 <= nx <=100000 and visited[nx] == 0 :
                visited[nx] = visited[x]+1
                q.append(nx)
                if nx == k : 
                    return visited[x]
               

print(bfs())