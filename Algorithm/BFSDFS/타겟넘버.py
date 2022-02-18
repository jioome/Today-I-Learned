
def solution(numbers, target):
    answer = 0 
    n = len(numbers)
    def dfs(idx,result):
        if idx == n :
            if result == target : 
                nonlocal answer 
                answer += 1 

    
    dfs(0,0)

    return answer




solution([1, 1, 1, 1, 1],3)
