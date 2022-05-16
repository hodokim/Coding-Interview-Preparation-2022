def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees :
        idx = 0
        chk_data = ''
        for skill_point in tree :
            if skill_point in skill :
                chk_data += skill_point
                if chk_data[idx] != skill[idx] :
                    chk_data = '99'
                    break            
                idx += 1
        if chk_data != '99' : answer += 1
        
    return answer