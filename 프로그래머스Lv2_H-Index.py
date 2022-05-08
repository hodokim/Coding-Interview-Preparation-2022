def solution(citations):
    citations.sort()
    ansList = []
    for(idx, x) in enumerate(citations):
        if(x <= len(citations[idx:])):
            ansList.append(x)
        elif(x > len(citations[idx:])):
            ansList.append(len(citations[idx:]))
            
    return max(ansList)