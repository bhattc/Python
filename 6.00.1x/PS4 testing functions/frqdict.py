sequence = 'pet'
word = "chayote"
hand = {'a': 1, 'c': 2, 'u': 2, 't': 2, 'y': 1, 'h': 1, 'z': 1, 'o': 2}
l = []
w = []
WORDLIST_FILENAME = "words.txt"
tothand = 0

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    
    for x in sequence:
        hand[x] = hand.get(x,0) + 1
    updatehand(hand, word)
    print hand
    print "freq function"
    #return hand

def updatehand(hand, word):
    #prev = ''

    if word not in w:
        w.append(word)
        print w
    else:
        print "already have a word inside"
        return False
    for c in word:
        print c
        if c in hand:
            #if p != word:
                #print hand[c]
            if hand[c] > 0:
                hand[c] -= 1
                
                isValidWord(word, hand, wordList)
            else:
                return False
        else:
            return False
            #l.append(c)
            #print l
            #print w
    #p = ''.join(l)
        #prev = word
        #return hand
        #print "update function"
        
    #else:
        
def isValidWords(word, hand, wordList):
    #tothand = 0
    #w = []
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    #for line in fil:
     #   print line
    #if word not in w:
    #    w.append(word)
        #print word
    #for h in hand:
    #    global tothand
     #   tothand += hand[h]
        #print tothand
      #  if tothand == 0:
    if word in wordList:
            #print wordList
        print "word found"
        return True
    else:
        print "Not a word"
        return False
        
        #else:
         #   return True


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    #for line in fil:
     #   print line
    if word not in w:
        w.append(word)
        #print w
    else:
        #print "already have a word inside"
        return False
    for z in word:
        print z
        if z in hand:
            #if p != word:
                #print hand[c]
            if hand[z] > 0:
                hand[z] -= 1
                
            else:
                return False
        else:
            return False
    if word in wordList:
        print "here is true"
        return True
    else:
        return False



wordList = loadWords()
