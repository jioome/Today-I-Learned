


def solution(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    answer = 0 
    print(queue[1])
    while True : 
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue) :
            queue.append(cur)
        else : 
            answer += 1 
            if cur[0] == location : 
                return answer 



solution([2, 1, 3, 2],	2)