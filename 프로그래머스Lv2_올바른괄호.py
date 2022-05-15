def solution(s):
    n = 0
    
    for x in s :
        if x == '(' :
            n += 1
        if x == ')' :
            n -= 1
        if n == -1 :
            return False
    
    if n == 0 :
        return True

    return False