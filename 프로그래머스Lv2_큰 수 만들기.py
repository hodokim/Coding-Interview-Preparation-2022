def solution(number, k):   
    ansList = []
    
    for (i, num) in enumerate(number):
        while ansList and k>0 and num > ansList[-1] :
            del ansList[-1]
            k -= 1
        
        if k == 0 :
            ansList += number[i:]
            break
        
        ansList.append(num)
    
    if k > 0 :
        ansList = ansList[:-k]

        
    answer = ''.join(ansList)
            
    return answer