def solution(s):
    stack_data = []
    
    for i in range(len(s)) :
        if not stack_data :
            stack_data.append(s[i])
        else : 
            if stack_data[-1] == s[i] :
                stack_data.pop()
            else :
                stack_data.append(s[i])
    
    if stack_data : answer = 0
    else : answer = 1
        
    return answer