def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        print(citations[i],l-i)
        if citations[i] >= l-i:
            print(l-i)
            return l-i
    return 0


solution([0,1,2,5,6])