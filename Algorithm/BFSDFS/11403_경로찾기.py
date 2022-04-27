import sys
sys.stdin =open('in.txt','rt')
input = sys.stdin.readline

n = int(input())
graph = [] 

for _ in range(n) : 
    graph.append(list(map(int,input().split())))

#플로이드워셜 알고리즘 
for k in range(n): # 모든 정점을 확인하기 위해 k 사용 
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j] : # 어느 한 곳에 들려 다른 곳으로 가는 길이 존재한다면 그 값을 체킹
                graph[i][j] = 1 


                
for i in graph : 
    for j in i : 
        print(j,end=' ')
    print()
