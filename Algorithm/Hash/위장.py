
def solution(clothes):
    answer = 1
    closet= {} 
    for i in clothes : 
        key = i[1]
        value = i[0]
        if key in closet : 
            closet[key].append(value)
        else :
            closet[key] = [value]
    
    print(closet)
    for key in closet.keys():
        answer = answer * (len(closet[key])+1)


    answer -=1 
    return  answer

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])