
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int,map(''.join,permutations(list(n),i+1))))
    
    a -= set(range(2))

    for i in range(2,max(a)//2 +1):
        a-= set(range(i*2,max(a)+1,i))
    return len(a)
solution("17")