# 시간 복잡도가 안좋았다. O(n)
def solution(A):
    # write your code in Python 3.6
    compare = []
    for i in A:
        if i not in compare:
            compare.append(i)
        else:
            del compare[compare.index(i)]
    print(compare)
    return int(compare[0])


solution([9, 3, 9, 3, 9, 7, 9])
