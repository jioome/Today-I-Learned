import sys
input = sys.stdin.readline 

n = int(input())
p = [0]+list(map(int, input().split()))
# max_prices = p 하면, 복사가 아니라 참조가 되어
# 한 곳을 변경하면 다른 곳도 똑같이 변경된다.
# (이 코드에서는 참조로 해도 이상은 없음.)
max_prices = p[:]

for i in range(2, n + 1):
    for j in range(1, i // 2 + 1):
        if max_prices[i] < max_prices[i - j] + max_prices[j]:
            max_prices[i] = max_prices[i - j] + max_prices[j]

print(max_prices[n])