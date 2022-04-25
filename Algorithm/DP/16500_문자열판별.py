def sol(idx):
    global result
    if idx == len(S):
        result = 1
        return
    if dp[idx]:
        return
    dp[idx] = 1
    for i in range(len(A)):
        if len(S[idx:]) >= len(A[i]): # S가 더 길 때만 비교 가능 
            for j in range(len(A[i])): # A에 포함된 단어 
                if A[i][j] != S[idx+j]:
                    break
            else:
                sol(idx+len(A[i]))
    return
    
S = input()
A = []
dp = [0] * 101 # 메모제이션 
for _ in range(int(input())):
    A.append(input())
result = 0
sol(0)
print(result)