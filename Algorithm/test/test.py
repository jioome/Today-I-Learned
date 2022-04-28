

import sys
sys.stdin =open('in.txt','rt')
input = sys.stdin.readline 
sys.setrecursionlimit(1000000)

t = int(input())


def dfs(i):
    visited[i] = 1
    cycle.append(i)
    global result 
    
    if visited[student[i]]:
        if student[i] in cycle:
            result += cycle[cycle.index(student[i]):]
            return 
    else : 
        dfs(student[i])

for _ in range(t):
    n = int(input())
    visited = [0]*(n+1)
    student = [0] + list(map(int,input().split()))
    
    result = [] 
    for i in range(1,n+1):
        if visited[i] == 0 : 
            cycle = [] 
            dfs(i)
    print(n-len(result))
