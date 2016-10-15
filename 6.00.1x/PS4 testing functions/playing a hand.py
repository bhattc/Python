import sys
#hand = {'k': 1, 'c': 1, 'u': 1, 'd': 1}
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
listofwords=[]
total = 0
newn=0
finaltotal = 0
WORDLIST_FILENAME = "words.txt"
n=0
def loadWords():
    #newn = n
    #newn = 2
    #print str(newn) + " value of newn initially"
    print "loading words"
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
def showhand(hand):
    global n
    #print "welcome to showhand"
    for letterinhand in hand:
        
        for valuesofhand in range (0,hand[letterinhand]):
            print letterinhand,
    print ""
    #print "total number of n:" +str(n)


def isValidWord(word, hand, wordList, n):
    
    #print "welcome to isvalidword"
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    global newn
    # TO DO ... <-- Remove this comment when you code this function
    
    if word in wordList:
        #print "here is true"
        #print " Found word"
        
        for letterofword in word:
            if letterofword in hand:
                
                #print n
        
                if hand[letterofword] <= 0:
                    print "Invalid word, please try again.1"
                    playHand(hand, wordList, n)
                    
                    #print n     
                
                    
            else:
                print "Invalid word, please try again.2"
                playHand(hand, wordList, n)
        for letterinword in word:
            hand[letterinword] -= 1
            newn += 1
        getWordScore(word, n)
        if word not in listofwords:
            listofwords.append(word)
            #print w
        else:
            #print "already have a word inside"
            print "Word you have already checked"
        #print newn
        if newn == n:
            #print str(word) +' earned  ' + str(total)+' points. Total:' +str(finaltotal)+ ' points.'
            #print str(n) + " value of n at n==0 condition"
            print "Run out of letters. Total score: "+str(finaltotal)+" points. "
            
        else:
            playHand(hand, wordList, n)

    else:
        print "Invalid word, please try again.3"
        playHand(hand, wordList, n)
def getWordScore(word, n):
    total = 0
    global newn,finaltotal
    #print "welcome to getwordscore"
    global total
        
            
    l = list(word)
        #print l
    for w in l:
        #n -=1
        #   print w
            #print SCRABBLE_LETTER_VALUES[w]
        total += SCRABBLE_LETTER_VALUES.get(w,0)
        #print total
    total = total * len(l)
    finaltotal += total
    #print str(len(l)) + " value of length of a word in get score function"
    #print str(newn) + " value of newn which is checking with a lenth of a word"
    if len(l) == n:
        finaltotal += 50
        print str(word) +' earned  ' + str(total)+' points. Total:' +str(finaltotal)+ ' points.'

        #print finaltotal
    else:
        print str(word) +' earned  ' + str(total)+' points. Total:' +str(finaltotal)+ ' points.'

def playHand(hand, wordList, n):
    #print "in playhand"
    #print n
    global newn
    
    
    #print newn
    word = ""
    showhand(hand)
    inputword = raw_input('Enter word, or a "." to indicate that you are finished:')
    for singleletter in inputword:
        
        if singleletter != '.':
            word += singleletter
            
        else:
            print "Goodbye! Total score:" + str(finaltotal)+" points."
            sys.exit("")
    #return word
    isValidWord(word, hand, wordList, n)
    
    #print word
print SCRABBLE_LETTER_VALUES
wordList = loadWords()
playHand({'c': 1, 'b': 1, 'e': 1, 'h': 1, 'l': 1, 'o': 1, 'n': 1, 's': 2, 'v': 1}, wordList, 10)
