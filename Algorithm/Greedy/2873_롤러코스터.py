r,c = map(int,input().split())

g = [list(map(int,input().split())) for _ in range(r)]

U,R,L,D = [[-1,0],[0,1],[0,-1],[1,0]]

# r,c 중 하나가 홀수 -> 모든 칸 방문 가능 
if r % 2 ==1 : 
    print((c-1)*"R"+"D" + ((c-1)*"L"+"D"+(c-1)*"R"+"D")* ((r-1)//2))
elif c % 2 == 1 : 
    print((r-1)*"D"+"R" + ("R"+(r-1)*"U"+"R"+(r-1)*"D")*((c-1)//2))
# 둘 다 짝수일 경우 
else : 
    low = 1000
    position = [-1, -1]

    for i in range(r):
        for j in range(c):
            if (i+j)%2 == 1 and low > g[i][j]:
                low = g[i][j]
                position = [i, j]
    
    # x(열) 기준 // 2
    res = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (position[1] // 2)
    x = 2 * (position[1] // 2)
    y = 0
    # 홀수를 짝수로 만들어준다음 무조건 오른쪽 1칸을 이동해야하는 과정이 있기 때문에
    xbound = 2 * (position[1] // 2) + 1

    while x != xbound or y != r - 1:
        if x < xbound and [y, xbound] != position:
            x += 1
            res += 'R'
        elif x == xbound and [y, xbound - 1] != position:
            x -= 1
            res += 'L'
        if y != r - 1:
            y += 1
            res += 'D'

    res += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - position[1] - 1) // 2)

    print(res)