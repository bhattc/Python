secretWord = 'escap'
lettersGuessed =  ['e', 'p', 'c', 'm', 's', 'u', 'i', 'd', 'a', 'r']
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    a = []
    t = 0
    f = 0
    u = '_'
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #for x in range(0,len(secretWord)):
     #   a.append(u)
    if len(lettersGuessed) > 0:
        #for p in range (0,len(secretWord)):
            #print 'Comparing ' + secretWord[p] + ' now'
            for q in range(0,len(lettersGuessed)):
                #print 'comparing with ' + lettersGuessed[q]
                #print secretWord[p]
                #print lettersGuessed[q]
                for g in l:
                    if g == lettersGuessed[q]:
                        l.remove(lettersGuessed[q])
                #if secretWord[p] != lettersGuessed[q]:
                #    f += 1
                    
                
                #else:
                 #   t += 1
                  #  a[p] = secretWord[p]
                    
                    #print 'Found ' + lettersGuessed[q]
                    #print a
                   #break
        #if t == len(secretWord):
         #   d = ' '.join(a)
            e = ''.join(l)
            
            return e
          #  #return True
        #else:
            
         #   d = ' '.join(a)
          #  e = ''.join(l)
           # return e
        
    else:
        #d = ' '.join(a)
        e = ''.join(l)    
        return e
