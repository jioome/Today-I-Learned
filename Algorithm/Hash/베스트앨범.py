def solution(genres, plays):
    answer = []
    gen_list = {}
    total_list = {} 
    num_gen = len(genres)
    for i in range(num_gen):
        if genres[i] in total_list : 
            total_list[genres[i]].append((plays[i],i))
            gen_list[genres[i]] += plays[i]
        else : 
            total_list[genres[i]] = [(plays[i],i)]
            gen_list[genres[i]] = plays[i]
        
    gen_list = sorted(gen_list.items(),key = lambda x : x[1] ,reverse = True)
    
    for i in total_list : 
        total_list[i] = sorted(total_list[i] ,key = lambda x : x[0] ,reverse = True)[:2]
    print(total_list)
    print(gen_list)
    while gen_list : 
        genre_max = gen_list.pop(0)
        for t in total_list : 
            if t == genre_max[0] : 
                if len(total_list[t])> 1 : 
                    answer.append(total_list[t][0][1])
                    answer.append(total_list[t][1][1])
                else : 
                    answer.append(total_list[t][0][1])
    
    
            
    return answer
solution(["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 500, 2500])