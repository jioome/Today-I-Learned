import sys
from collections import deque
import sys
sys.stdin = open('in.txt', 'rt')

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    q = deque()
    q.append((a, ''))
    visited = [False]*10000

    while q:
        num, path = q.popleft()
        visited[num] = True
        if num == b:
            print(path)
            break

        num2 = (2*num) % 10000
        if not visited[num2]:
            q.append((num2, path+"D"))

        num2 = (num-1) % 10000
        if not visited[num2]:
            q.append((num2, path+"S"))

        num2 = (10*num+(num//1000)) % 10000
        if not visited[num2]:
            q.append((num2, path+"L"))

        num2 = (num//10+(num % 10)*1000) % 10000
        if not visited[num2]:
            q.append((num2, path+"R"))
