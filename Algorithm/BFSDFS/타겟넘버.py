
def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    print(answer)
    return answer

def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        
        if sum(numbers) == target:
            print(numbers)
            return 1
        else: return 0
    else:
        answer += DFS(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        return answer


solution([1, 1, 1, 1, 1],3)
