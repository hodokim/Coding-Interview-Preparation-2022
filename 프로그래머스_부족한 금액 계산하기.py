def solution(price, money, count):
    totalPrice = 0
    countList = [0] * count
    for idx,x in enumerate(countList):
        totalPrice += price * (idx+1)
    
    pay = totalPrice - money
    answer = max(pay, 0)

    return answer