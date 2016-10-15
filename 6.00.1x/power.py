
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    # Your code here
    while exp > 0:
        result *= base 
        exp -= 1
        
    return result


y = iterPower(3,2)
print y
