import sys
sys.stdin = open('in.txt', 'rt')
n, m = map(int, input().split())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def uion_team(parent, a, b):
    c = find_parent(parent, a)
    d = find_parent(parent, b)
    if c > d:
        parent[b] = c
    else:
        parent[a] = d


parent = []
for i in range(n+1):
    parent.append(i)

for i in range(m):
    operate, a, b = map(int, input().split())
    if operate == 0:
        # 팀 합치기
        uion_team(parent, a, b)

    if operate == 1:
        # 팀 여부 확인
        if find_parent(parent, a) == find_parent(parent, b):
            result = True
        else:
            result = False

        if result == True:
            print("YES")

        else:
            print("NO")


# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
