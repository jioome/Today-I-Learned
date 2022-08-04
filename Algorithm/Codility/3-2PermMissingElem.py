# 효율성 검사에서
def solution(A):
    A.sort()
    if len(A) == 0:
        return 1
    for i in range(len(A)):
        if A[i] != i+1:
            return i+1
    return len(A)+1


print(solution([1]))
