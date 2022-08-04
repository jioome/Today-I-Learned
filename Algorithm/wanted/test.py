

import sys
sys.stdin = open('in.txt', 'rt')

input = sys.stdin.readline
n, k = map(int, input().split())
# 몬스터의 공격력
power = list(map(int, input().split()))
# 마을의 주민 수
p_num = list(map(int, input().split()))

power_list = []
for i in range(n):
    power_list.append((power[i], p_num[i]))
power_list.sort()
answer = 0
sump = 0
for p, n in power_list:
    sump += p
    k -= sump
    if k >= 0:
        answer += n
    else:
        break

print(answer)
