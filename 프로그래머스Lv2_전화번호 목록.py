def solution(book):
    book.sort()
    
    for b1, b2 in zip(book, book[1:]):
        if(b2.startswith(b1)):
            return False
            
    return True