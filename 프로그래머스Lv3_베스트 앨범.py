def solution(genres, plays):
    answer = []

    dic_1 = {}
    dic_2 = {}
    
    for idx, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic_1 :
            dic_1[g] = p
        else :
            dic_1[g] += p
        
        if g not in dic_2 :
            dic_2[g] = [(idx, p)]
        else :
            dic_2[g].append((idx, p))

    for(key, value) in sorted(dic_1.items(), key=lambda x:x[1], reverse=True) :
        for(i, p) in sorted(dic_2[key], key=lambda x:x[1], reverse=True)[:3] :
            answer.append(i)

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 500, 800, 2500]

solution(genres,plays)