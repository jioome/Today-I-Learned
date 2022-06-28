
def solution(A, K):
    # write your code in Python 3.6
    answer = [0]*len(A)
    for i in range(len(A)):
        idx = (i+K)
        if idx >= len(A):
            idx = idx % len(A)
        answer[idx] = A[i]
    print(answer)


solution([0, 0, 0], 1)
