#aTup = ('I', 'am', 'a', 'test', 'tuple')
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    t1 = ()
    for c in range(0,len(aTup)):
       
        if c % 2 == 0:
            t1 = t1 + (aTup[c],)
            c +=2
    return t1
