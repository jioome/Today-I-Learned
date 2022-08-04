# 효육성 검사에서
def solution(A):
    for i in range(1, len(A)+2):
        if i not in A:
            print(i)
            return i


solution([2, 3, 1, 5])
