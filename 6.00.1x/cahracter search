def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False


    if len(aStr) == 1:
        return char == aStr


    mid = len(aStr)/2
    midcha = aStr[mid]
    if char == midcha:
        return True


    elif char < midcha:
        return isIn(char, aStr[:mid])


    else:
        return isIn(char,aStr[mid+1:])
