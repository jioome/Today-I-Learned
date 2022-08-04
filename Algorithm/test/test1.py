# dfs
def dfs(computers, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    computers[x][y] = 2
    computers[y][x] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(computers) and 0 <= ny < len(computers) and computers[nx][ny] == 1:
            dfs(computers, nx, ny)


def solution(n, computers):
    answer = 0

    for x in range(n):
        for y in range(n):
            if computers[x][y] == 1:
                dfs(computers, x, y)
                answer += 1

    return answer
