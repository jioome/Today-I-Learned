def solution(brown, yellow):
    answer = []
    S = brown + yellow
    for i in range(1,S//2):
        if S % i == 0 :
            h = i
            w = S //h
        if (h-2)*(w-2) == yellow:
            return [w,h]
        
    return answer
solution(10, 2)