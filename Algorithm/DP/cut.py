

def solution(n, times):
    dp = [0] + [times[0] * i for i in range(n)]
    # dp[i] 는 i 개의 줄 만드는데 걸린 시간
    # dp[0] -> 그냥 배열 맞춰 주려고 넣음
    # dp[1]은 그냥 한 줄 짜리 아무 것도 안 자른 것 / dp[1] = 0
    # dp[2]은 한 번 자른 것 / dp[2] = times[0] 한 개 자른 시간

    for i in range(3, n+1):  # dp[3] 부터 dp[n]까지 구한다.
        for j in range(len(times)):  # j 번째 있는 것은 줄 j+1 개 자르는데 걸리는 시간
            if i-(j+1) >= (j+1):   # j+1 : 자르는 줄의 개수
                a = dp[i-(j+1)] + times[j]  # 걸리는 시간
                dp[i] = min(a, dp[i])

    # 답은 dp[n]
    return dp[n]


print(solution(4, [2, 3]))
print(solution(5, [2, 4, 5]))
print(solution(6, [1, 2, 3]))

# 5,8,5

# dp[i] 는 i 개의 줄 만드는데 걸린 시간
# dp[4] = dp [3] + time[0]  자르는 줄의 개수 1
# dp[4] = dp [2] + time[1]  자르는 줄의 개수 2
# dp[4] = dp [1] + time[2]? 자르는 줄의 개수 3 /  안됨 왜냐면 줄이 하나 뿐 ,,,,
# 4-(2+1) >= (2+1) 성립하지 않는다.
