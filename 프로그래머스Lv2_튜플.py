def solution(s):
    answer = []
    new_s = s.replace('{', '')
    new_s = new_s.replace('}','')
    new_s = new_s.split(',')  
    temp_dic = {}
    
    for i in new_s :
        if i in temp_dic :
            temp_dic[i] += 1
        else :
            temp_dic[i] = 1
            
    data = sorted(temp_dic.items(), key=lambda x: x[1], reverse=True)
    
    for key in data :
        answer.append(int(key[0]))
        
    return answer