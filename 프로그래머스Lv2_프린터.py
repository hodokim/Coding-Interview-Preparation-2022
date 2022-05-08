def solution(priorities, location):
    answer = 0
    idxList = [idx for idx in range(len(priorities))]
    queueList = priorities.copy()
    
    i = 0
    while True :
        if queueList[i] < max(queueList[i+1:]):
            idxList.append(idxList.pop(i))
            queueList.append(queueList.pop(i))
        else :
            i += 1
        
        if queueList == sorted(priorities, reverse=True):
            break
    
    answer = idxList.index(location)+1
      
    return answer