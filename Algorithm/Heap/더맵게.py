import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K : 
        if len(scoville) == 1  :
            return -1
        first_min=heapq.heappop(scoville)
        second_min=heapq.heappop(scoville)

        heapq.heappush(scoville,first_min + second_min*2)
        first_min = scoville[0]

        answer += 1
        
    print(answer)

    return answer

solution([1, 2, 3, 9, 10, 12],	7)