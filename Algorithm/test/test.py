import sys
input = sys.stdin.readline 

n = int(input())
p = [0]+list(map(int, input().split()))
max_p = p[:]
for i in range(2,n+1):
    for j in range(1,i//2 + 1 ):
        max_p[i] = max(max_p[i-j]+max_p[j],max_p[i])
print(max_p[n])