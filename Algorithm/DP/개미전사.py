n = int(input())
food = list(map(int, input().split()))
dp = [0]*n
dp[0] = food[0]
dp[1] = max(dp[0], food[1])
for i in range(2, n):
    dp[i] = max(food[i]+dp[i-2], dp[i-1])


print(dp[n-1])
