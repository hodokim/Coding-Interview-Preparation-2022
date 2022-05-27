def solution(cacheSize, cities):
    answer = 0
    sizeChk = 0
    cache = []
    
    if cacheSize == 0 :
        return len(cities) * 5
    
    for c in cities :
        city = c.upper()
        if city in cache :
            answer += 1
            cache.remove(city)
            cache.append(city)
        else :
            answer += 5
            if sizeChk < cacheSize :
                cache.append(city)
                sizeChk += 1
            else :
                cache.pop(0)
                cache.append(city)
                          
    return answer