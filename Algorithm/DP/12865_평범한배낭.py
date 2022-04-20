import sys 
input = sys.stdin.readline 
n,k = map(int,input().split())
bag=[[0,0]]
for i in range(n):
    thing = list(map(int,input().split()))
    bag.append(thing)


dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        w = bag[i][0]
        v = bag[i][1]
        if j < w : # 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다
            dp[i][j] = dp[i-1][j]
        else : 
            dp[i][j] = max(dp[i-1][j-w]+v,dp[i-1][j])


print(dp[n][k])