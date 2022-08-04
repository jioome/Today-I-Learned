

import sys

sys.stdin = open('wanted3.txt', 'rt')

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = 0

print(combinations(a, 2))
