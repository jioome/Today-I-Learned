def dfs(n,computers,start,visited):
    visited[start] = True
    for i in range(n):
        if visited[i] == False and computers[start][i] == 1 :
            visited = dfs(n,computers, i,visited)
    return visited


def solution(n, computers):
    answer = 0
    visited = [False] * n 

    for start in range(n):
        if visited[start] == False : 
            dfs(n,computers,start,visited)
            answer += 1 
    
    return answer

solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]])