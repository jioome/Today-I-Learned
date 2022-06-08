
import sys
sys.stdin =open('in.txt','rt')
input = sys.stdin.readline 

minutes = [] 
p = 0 
answer = 0 
for i in range(11):
    a,b = map(int,input().split())
    minutes.append(a)
    p += b 

minutes.sort()
cur = 0 
result = 0 
for i in range(len(minutes)):
    cur += minutes[i]
    result += cur 



answer =  result +  (20 * p)
print(answer)
