import heapq

def solution(sco, k):
    heapq.heapify(sco)
    made = 0
    cnt = 0
    
    while len(sco) >= 2:
        min_1 = heapq.heappop(sco)
        
        if(min_1 >= k):
            return cnt
        
        if(min_1 < k):
            min_2 = heapq.heappop(sco)
            made = min_1 + (min_2 * 2)
            heapq.heappush(sco, made)
            cnt += 1
            
    min_last = heapq.heappop(sco)
    if(min_last < k):
        return -1
    else:
        return cnt