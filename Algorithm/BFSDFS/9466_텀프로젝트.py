import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
t = int(input())

def dfs(i):
    cycle.append(i)
    global result 
    visited[i] = True 
    if visited[student[i]]:
        if student[i] in cycle :
            result += cycle[cycle.index(student[i]):]
            return 
    else : 
        dfs(student[i])




for i in range(t):
    
    n =int(input())
    visited = [False] * (n+1)
    student = [0] + list(map(int,input().split()))
    result = [] 

    for i in range(1,n+1):
        if visited[i] == False : 
            cycle = []
            dfs(i)
    print(n-len(result)) 