location = input()
# 문자를 유니코드 정수로 바꾸기 : ord
col = int(ord(location[0])-97)
row = int(location[1])-1

chess = [[0]*(8)for _ in range(8)]

cnt = 0
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

for i in range(8):
    nx = row + dx[i]
    ny = col + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        cnt += 1
print(cnt)
