

import sys

sys.stdin = open('wanted3.txt', 'rt')

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = 0

for i in range(n):
    suma = 0
    sumb = 0
    for j in range(i, n):

        suma += a[j]
        sumb += b[j]
        if suma == sumb:
            answer += 1

print(answer)
