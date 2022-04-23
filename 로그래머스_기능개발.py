import math

def solution(progresses, speeds):
    workDays = []
    remainDay = 0
    answer = []
    chkPoint = 0
    
    for idx, x in enumerate(progresses) :
        remainDay = (100-x) / speeds[idx]
        remainDay = math.ceil(remainDay)
        workDays.append(remainDay)
                                  
    for i in range(len(workDays)):
        if(workDays[chkPoint]<workDays[i]):
            answer.append(i-chkPoint)
            chkPoint = i
    
    answer.append(len(workDays)-chkPoint)
        
        
                                                                                
    return answer