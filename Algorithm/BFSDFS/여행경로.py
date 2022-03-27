
def solution(tickets):
    
    routes = dict()
    answer = [] 
    for ticket in tickets:
        if ticket[0] in routes : 
            routes[ticket[0]].append(ticket[1])
        else : 
            routes[ticket[0]] = [ticket[1]]
    for i in routes.keys() : 
        routes[i].sort(reverse=True)

    start = ["ICN"]
    while start : 
        target = start[-1]
        if target not in routes or len(routes[target])== 0:
            answer.append(start.pop())
        else : 
            start.append(routes[target].pop())
    print(answer)
    return answer[::-1]

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])