A = input()
number = list(map(int,input().split()))
dp = number[:]
for i in range(len(number)):
    for j in range(i):
        if number[i] > number[j] : 
            dp[i] =  max(dp[i],number[i] +  dp[j])

print(max(dp))
            
