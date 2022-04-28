

import sys
sys.stdin =open('in.txt','rt')

e,s,m = map(int,input().split())
num = 15*28*19
for year in range(1,num+1): 
    if (year-e)%15 == 0 and (year-s)%28 == 0 and (year-m)%19 == 0 : 
        print(year)
        break