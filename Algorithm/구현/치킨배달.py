import sys
from itertools import combinations
sys.stdin = open('in.txt', 'rt')
input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = float("inf")
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        if city[i][j] == 2:
            chicken.append([i, j])
chi_length = []
distance = 0
for ch in combinations(chicken, m):
    distance = 0
    for h in house:
        sumc = float('inf')
        for c in ch:
            sumc = min(abs(h[0]-c[0])+abs(h[1]-c[1]), sumc)
        distance += sumc
    chi_length.append(distance)
result = int(min(chi_length))
print(result)
