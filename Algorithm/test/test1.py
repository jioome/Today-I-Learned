import sys
from collections import deque
import sys
sys.stdin = open('in.txt', 'rt')

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    q = deque()
    path = ''
    visited = [0]*10000
    q.append((a, ''))
    while q:
        num, path = q.popleft()
        if num == b:
            print(path)
            break
        visited[num] = 1
        num2 = (num*2) % 10000
        if visited[num2] == 0:
            q.append((num2, path+"D"))

        num2 = (num-1) % 10000
        if visited[num2] == 0:
            q.append((num2, path+"S"))

        num2 = (num*10 + +(num//1000)) % 10000
        if visited[num2] == 0:
            q.append((num2, path+"L"))

        num2 = (num % 10)*1000 + (num//10)
        if visited[num2] == 0:
            q.append((num2, path+"R"))
