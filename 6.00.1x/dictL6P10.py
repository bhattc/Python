animals = { 'a': ['aardvark'], 'b': ['baboon',13], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    store = []
    n = 0
    for i in animals:
    #for value in animals.values():
        h = 0
        for p in animals[i]:
        # h += len(value)  
            h += 1
        if h > n:
            n = h
            store = i
    return store 
