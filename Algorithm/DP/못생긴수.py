n = int(input())
dp = []
dp.append(1)

for i in range(1, n):
    if not dp[i-1]*2 in dp:
        dp.append(dp[i-1]*2)
    if not dp[i-1]*3 in dp:
        dp.append(dp[i-1]*3)
    if not dp[i-1]*5 in dp:
        dp.append(dp[i-1]*5)
    dp.sort()
    if len(dp) >= n:
        break

print(dp[n-1])
