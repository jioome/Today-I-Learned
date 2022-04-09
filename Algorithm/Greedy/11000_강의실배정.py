import heapq,sys
time = [] 
room = []
input = sys.stdin.readline # 시간초과 문제 
n = int(input())
for i in range(n):
    time.append(list(map(int,input().split())))
time.sort()
heapq.heappush(room,time[0][1])
for i in range(1,len(time)) : 
    if room[0] <= time[i][0] :
        heapq.heappop(room)
        heapq.heappush(room,time[i][1])
    else : 
        heapq.heappush(room,time[i][1])
print(len(room))
     



    




