
def solution(A):
    # write your code in Python 3.6
    dif = float('inf')
    for p in range(1, len(A)):
        first = sum(A[:p])
        second = sum(A[p:])
        dif = min(dif, abs(first-second))
    return dif


print(solution([3, 1]))
