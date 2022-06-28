from array import array
import sys
sys.stdin = open('in.txt', 'rt')
n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]


# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 1
visited[x][y] = 1
turn_time = 0


def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if visited[nx][ny] == 0 and graph[nx][ny] == 0:
        count += 1
        visited[nx][ny] = 1
        x = nx
        y = ny
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if graph[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)
