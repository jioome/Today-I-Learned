
def solution(A):
    # write your code in Python 3.6
    dif = float('inf')
    first = 0
    second = sum(A)
    for p in range(len(A)-1):
        first += A[p]
        second -= A[p]
        dif = min(dif, abs(first-second))
    return dif


print(solution([3, 1]))
