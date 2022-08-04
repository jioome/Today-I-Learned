import math


def solution(X, Y, D):
    # write your code in Python 3.6
    dif = X-Y
    result = math.ceil(dif/D)
    return result
