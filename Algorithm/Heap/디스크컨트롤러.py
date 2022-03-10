import heapq

def solution(jobs):
    answer = 0
    now,i  = 0,0
    start = -1 
    heap = [] 
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장 
        for j in jobs:
            if start < j[0] <= now : 
                heapq.heappush(heap,[j[1],j[0]])
        if len(heap) > 0: #처리할 작업이 있을 때 
            cur = heapq.heappop(heap)
            start = now  
            now += cur[0]
            answer += now - cur[1]
            i += 1 
        else : #처리할 작업이 없는 경우 
            now +=1 
    print(answer //i)

    return answer //i

solution([[0, 3], [1, 9], [2, 6]])