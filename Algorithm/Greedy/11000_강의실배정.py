import heapq
time = [] 
room = []
lecture = 0 
n = int(input())
for i in range(n):
    time.append(list(map(int,input().split())))
time.sort()
for s,t in time : 
    if len(room) == 0 : 
        heapq.heappush(room,t)
        lecture += 1
        continue 
    elif room[0] <= s :
        heapq.heappop(room)
        heapq.heappush(room,t)
    else : 
        heapq.heappush(room,t)
        lecture += 1 
print(lecture)
     



    




