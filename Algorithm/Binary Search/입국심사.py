def solution(n, times):
    answer = 0
    left = 1
    right = max(times)* n 
    while left < right :
        total = 0 
        mid = (left+right) //2 
        for t in times : 
            total += mid//t
        if total >= n : 
            right = mid
        else : 
            left = mid + 1 
        
    answer = left
    print(answer)


        
    
    return answer

solution(6,	[7, 10])