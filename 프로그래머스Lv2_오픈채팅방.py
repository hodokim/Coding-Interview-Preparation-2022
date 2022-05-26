def solution(record):
    answer = []
    users = {}
    logs = []
    
    for r in record :
        seq = r.split(' ')
        uid = seq[1]       
        if seq[0] == 'Enter' :
            logs.append((uid, 'E'))
            users[uid] = seq[2]
        elif seq[0] == 'Leave' :
            logs.append((uid, 'L'))
        else :
            users[uid] = seq[2]
            
    for log in logs :
        if log[1] == 'E' :
            answer.append(users[log[0]]+'님이 들어왔습니다.')
        elif log[1] == 'L' :
            answer.append(users[log[0]]+'님이 나갔습니다.')
                    
    return answer