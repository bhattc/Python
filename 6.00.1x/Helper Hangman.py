secretWord = 'apple'
lettersGuessed =  ['e', 'i', 'k', 'p', 'r', 's']
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    '''
    for p in range (0,len(secretWord)):
        print secretWord[p]
        print 'p is ' + str(p)
        for q in range (0,len(lettersGuessed)):
            print lettersGuessed[q]
            #secretWord[p] == lettersGuessed[q]
            if secretWord[q] != lettersGuessed[p]:
                 
                 print 'q is ' + str(q) + ' not in secretWord'
                 while q > len(lettersGuessed):
                     return False
            else:
                print lettersGuessed[q] + ' is in secretWord'  
                
                del lettersGuessed[q]
                p += 1
                #print p
                #print q
                
            break
                
                
    
    return True
    
    this one for comparing two strings togather whithout comparing all elements
    i = 0
    while i < len(secretWord): #in range (0,len(secretWord))
        print secretWord[i] 
        print lettersGuessed[i]
        if secretWord[i] != lettersGuessed[i]:
            return False
        else:
            i += 1
            print i
    return True
    '''
    #a = []
    t = 0
    f = 0
    #u = '_'
    #for x in range(0,len(secretWord)):
     #   a.append(u)
    if len(lettersGuessed) > 0:
        for p in secretWord:
            #print 'Comparing ' + p + ' now'
            for q in lettersGuessed:
                #print 'comparing with ' + lettersGuessed[q]
                #print secretWord[p]
                #print lettersGuessed[q]
                if p != q:
                    f += 1        
                
                else:
                    t += 1
                    #a[p] = secretWord[p]
                    print 'Found ' + q
                    break
        if t == len(secretWord):
            #print a
            return True
        else:
            return False
        
    else:
        return False
