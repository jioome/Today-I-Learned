# dfs가 끝난이후 해당 node를 방문했는지 확인하고 그룹수를 증가
def dfs(n,computers,start,visited):
    visited[start] = True
    for i in range(n):
        if computers[start][i] == 1 and visited[i] ==False:
            dfs(n,computers,i,visited)
    return visited


def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if visited[i] ==False:
            dfs(n,computers,i,visited)
            answer +=1 
    
    return answer

solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]])