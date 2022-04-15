from collections import deque

def bfs(n,computers,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue : 
        com = queue.popleft()
        visited[com] = True
        for i in range(n):
            if visited[i] == False and computers[com][i] == 1 :
                queue.append(i)

                
def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if visited[i] == False:
            bfs(n,computers,i,visited)
            answer +=1 
    return answer