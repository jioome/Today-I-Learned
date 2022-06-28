from collections import deque


n = int(input())
k = int(input())
apple = []
graph = [[0]*(n) for i in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 2
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

l = int(input())
direct = {}
for i in range(l):
    x, c = input().split()
    direct[int(x)] = c


def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4


queue = deque([(0, 0)])
cnt = 0
direction = 0
x, y = 0, 0
graph[x][y] = 1
while True:
    cnt += 1
    x = dx[direction] + x
    y = dy[direction] + y
    if x < 0 or x >= n or y < 0 or y >= n:
        break
    if graph[x][y] == 2:
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in direct:
            turn(direct[cnt])
    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        a, b = queue.popleft()
        graph[a][b] = 0

        if cnt in direct:
            turn(direct[cnt])

    else:
        break

print(cnt)
