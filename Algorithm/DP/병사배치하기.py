import sys
sys.stdin = open('in.txt', 'rt')
n = int(input())
army = list(map(int, input().split()))
dp = [1]*n
army.reverse()
for i in range(1, n):
    for j in range(i):
        if army[i] > army[j]:
            dp[i] = max(dp[i], dp[j]+1)


print(len(dp)-max(dp))
