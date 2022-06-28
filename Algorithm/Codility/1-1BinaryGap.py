def solution(N):
    bin_num = bin(N)
    list_one = []
    dist = 0
    print(type(bin_num))
    for i in range(len(bin_num)):
        if bin_num[i] == '1':
            list_one.append(i)

    if len(list_one) == 1 or len(list_one) == 0:
        return 0
    else:
        for i in range(1, len(list_one)):
            dist = max(dist, list_one[i]-list_one[i-1]-1)
        print(dist)
        return dist


solution(1041)
