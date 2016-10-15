def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        res = 1
        return res
    elif exp % 2 == 0:
        return  recurPower(base * base,exp/2)
    else:
        return base* recurPower(base,exp-1)
    #third case can be used for finding power for all if you sonr=t want to use that odd even method
