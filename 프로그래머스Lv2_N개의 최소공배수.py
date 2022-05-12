def solution(arr):
    answer = 0    
    n = 1
    
    while True :        
        answer = max(arr) * n
        chkFlag = True
                
        for i in arr :
            if(answer % i != 0):
                chkFlag = False
                break
                
        if chkFlag :
            break
            
        n += 1
        
    return answer