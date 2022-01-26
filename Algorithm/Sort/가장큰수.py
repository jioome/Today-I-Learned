from itertools import permutations

def solution(numbers):
    answer = ''
    pool = list(permutations(numbers,3))
    pool.sort()

    for i in pool:
        print(i)
    print(pool)

    return answer

solution([6, 10, 2])