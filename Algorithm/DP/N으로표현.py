def solution(N, number):
    if N == number:
        return 1

# 1. [SET*8] 초기화
    s = [set() for x in range(8)]

# 2. 각 set마다 기본 수 "N"*i 수 초기화
    for i,x in enumerate(s,start = 1):
        x.add(int(str(N)*i))
    print(s)

# 최솟값 구하기 
    for i in range(1,8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]: # 이전 것들과 사칙연산 
                    s[i].add(op1+op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0 :
                        s[i].add(op1 // op2)
        if number in s[i] :
            answer = i + 1
            break
        else : #최솟값 8보다 큰 경우 
            answer = -1
    return answer

solution(5,12)