

import sys
sys.stdin =open('in.txt','rt')
sys.setrecursionlimit(100000)
input = sys.stdin.readline 
n = int(input())
tree = [[]for _ in range(n+1)]

for i in range(1,n):
    a,b = map(int,input().split())
    tree[a].append(b) # 양쪽으로 다 연결되어 있음
    tree[b].append(a)

par = [-1]*(n+1) # 부모 노드 기록용 
def dfs(n):
    for i in tree[n] : 
        if par[i] == -1 : 
            par[i] = n 
            dfs(i)




dfs(1)
for i in range(2,n+1):
    print(par[i])
