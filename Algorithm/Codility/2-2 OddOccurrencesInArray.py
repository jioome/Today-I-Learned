# 시간 복잡도가 안좋았다. O(n)
def solution(A):
    # write your code in Python 3.6
    result = 0
    for i in A:
        result ^= i
    return result


print(solution([9, 3, 9, 3, 9, 7, 9]))
