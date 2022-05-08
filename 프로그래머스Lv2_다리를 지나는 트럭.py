def solution(bridge_length, weight, truck_weights):
    answer = 0
    lenList = []
    weightList = []

    lenList.append(0)
    weightList.append(truck_weights.pop(0))

    while truck_weights :
        for idx, x in enumerate(lenList):
            lenList[idx] += 1            
        answer += 1        
        if(lenList[0] > bridge_length):
            lenList.pop(0)
            weightList.pop(0)
        if(truck_weights[0] + sum(weightList) <= weight):
            lenList.append(1)
            weightList.append(truck_weights.pop(0))


    while lenList :
        for idx, x in enumerate(lenList):
            lenList[idx] += 1            
        answer += 1        
        if(lenList[0] > bridge_length):
            lenList.pop(0)
            weightList.pop(0)

    return answer