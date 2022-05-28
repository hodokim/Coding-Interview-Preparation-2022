def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n) :
        bin1 = bin(arr1[i]).replace('0b', '')
        bin2 = bin(arr2[i]).replace('0b', '')
        
        if(n != len(bin1)):
            bin1 = '0' * (n-len(bin1)) + bin1
        if(n != len(bin2)) :
            bin2 = '0' * (n-len(bin2)) + bin2
        
        temp = ''
       
        for j in range(n) :
            if(bin1[j] == '0' and bin2[j] == '0') :
                temp += ' '
            else :
                temp += '#'
            
        answer.append(temp)
        
        
    return answer