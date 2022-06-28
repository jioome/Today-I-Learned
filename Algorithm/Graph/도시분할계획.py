import sys
sys.stdin = open('in.txt', 'rt')
n, m = map(int, input().split())
# 최소 신장 트리
graph = []
count = 0

parent = []
for i in range(n+1):
    parent.append(i)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    a, b, fee = map(int, input().split())
    graph.append((fee, a, b))

graph.sort()
last = 0

for g in graph:

    fee, a, b = g
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        count += fee
        last = fee
print(count-last)
