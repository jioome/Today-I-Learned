r,c = map(int,input().split())

g = [list(map(int,input().split())) for _ in range(r)]

U,R,L,D = [[-1,0],[0,1],[0,-1],[1,0]]

# 홀수 
if r % 2 ==1 : 
    print((c-1)*'R'+"D" + ((c-1)*"L"+"D"+(c-1)*'R'+"D")*(r-1)//2)

elif c % 2 == 1 : 
    print((r-1)*'D'+"R" + ("R"+(r-1)*"U"+"R"+(r-1)*"D")*(c-1)//2)


print(g)