from itertools import combinations
def solution(number, k):
    answer = []
    for n in number : 
        while answer and answer[-1] < n and k>0 : 
            answer.pop()
            k-=1
        answer.append(n)
    answer = ''.join(answer[:len(number)-k])
    print(answer)

    return answer

solution("1924",	2)