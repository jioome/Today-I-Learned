# 파이썬
def attach(x, y, m, key, board):
    for i in range(m):
        for j in range(m):
            board[x+i][y+j] += key[i][j]


def detach(x, y, m, key, board):
    for i in range(m):
        for j in range(m):
            board[x+i][y+j] -= key[i][j]


def rotate90(arr):
    n = len(arr)
    m = len(arr[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result


def check(board, m, n):
    for i in range(n):
        for j in range(n):
            if board[m+i][m+j] != 1:
                return False
    return True


def solution(key, lock):
    m, n = len(key), len(lock)

    board = [[0] * (m*2 + n) for _ in range(m*2 + n)]
    # 자물쇠 중앙 배치
    for i in range(n):
        for j in range(n):
            board[m+i][m+j] = lock[i][j]

    rotated_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, m+n):
            for y in range(1, m+n):
                # 열쇠 넣어보기
                attach(x, y, m, rotated_key, board)
                # lock 가능 check
                if(check(board, m, n)):
                    return True
                # 열쇠 빼기
                detach(x, y, m, rotated_key, board)

    return False
