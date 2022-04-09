
def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance
    rocks.append(distance)
    rocks.sort()
    while left <= right : 
        mid = (left + right) // 2  # 거리의 최솟값을 mid로 잡음(거리가 mid 이하이면 다 없앤다)
        current, remove = 0,0 # 현재 위치 , 제거할 바위 수 
        min_distance = float('inf')

        for rock in rocks : 
            dis = rock-current
            if dis < mid : 
                remove +=1 
            else : 
                current = rock
                min_distance = min(min_distance,dis)
        
        if remove > n : 
            right = mid -1 
        else : 
            answer = min_distance
            left = mid + 1


    print(answer)        
    return answer


solution(25,[2, 14, 11, 21, 17]	,2)