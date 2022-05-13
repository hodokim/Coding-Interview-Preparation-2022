def solution(s):
    answer = ''
    tmp_list = []
    tmp_list = s.split()
    tmp_list = list(map(int,tmp_list))
    answer += str(min(tmp_list))
    answer += ' '
    answer += str(max(tmp_list))
    
    return answer