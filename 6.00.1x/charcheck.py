def isIn(char, aStr):
    
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    print aStr
    if aStr == '':
        print 'aStr is empty'
        return False
    
    if len(aStr) == 1:
        return char == aStr

    mid = len(aStr)/2
    print mid
    cha = aStr[mid]
    if char == cha:
        return True

    if char < cha:
        print aStr[:mid]
        return isIn(char, aStr[:mid])
    else:
        return isIn(char, aStr[mid+1:])
