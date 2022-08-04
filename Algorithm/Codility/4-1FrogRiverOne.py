
def solution(X, A):
    # write your code in Python 3.6
    check = set()
    for i in range(len(A)):
        check.add(A[i])
        if len(check) == X:
            return i
    return -1


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
