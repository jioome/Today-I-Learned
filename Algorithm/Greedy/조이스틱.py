def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]
    
    # 위 아래 조작 
    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    # 커서 좌우 이동 
    for idx in range(n):
        next_idx = idx + 1

        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        
        # idx 에서 되돌아 가는 경우 /  뒤에 있는 문자열부터 갔다오는 경우 ex) BBCAAAN
        distance = min(idx, n - next_idx)

        # 한 방향으로만 이동하는 경우와, 오른쪽으로 이동했다가 왼쪽으로 이동하는 경우를 비교
        move = min(move, idx  + distance+ n - next_idx)

    answer += move

    return answer
solution("JAAAAAAN")