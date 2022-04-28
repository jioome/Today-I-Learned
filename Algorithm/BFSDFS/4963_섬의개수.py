

import sys
sys.stdin =open('in.txt','rt')
input = sys.stdin.readline 
sys.setrecursionlimit(10000000)
dx = [1,-1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

def DFS(x, y):
        visitedList[x][y] = True  # 방문 완료

        for i in range(8): # 대각선까지 포함
            nX = x + dx[i]
            nY = y + dy[i]

            if 0 <= nX < h and 0 <= nY < w:
                if visitedList[nX][nY] == False and mapList[nX][nY] == 1:
                    DFS(nX, nY)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    mapList = []
    for i in range(h):
        mapList.append(list(map(int, input().split()))) # 지도 
    
    visitedList = [[False]*w for _ in range(h)]

    count = 0

    for i in range(h):
        for j in range(w):
            if visitedList[i][j] == False and mapList[i][j] == 1:
                DFS(i, j)
                count += 1

    print(count)