# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"
lettersGuessed = []
#v= ''
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = []


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
'''
def isWordGuessed(secretWord, lettersGuessed):

    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    
    # FILL IN YOUR CODE HERE...
    #a = []
    t = 0
    f = 0
    #u = '_'
    #for x in range(0,len(secretWord)):
     #   a.append(u)
    if len(lettersGuessed) > 0:

        for p in range(0,len(secretWord)):
            #print 'Comparing ' + p + ' now'
            for q in lettersGuessed:
                #print 'comparing with ' + lettersGuessed[q]
                #print secretWord[p]
                #print lettersGuessed[q]
                if secretWord[p] != lettersGuessed[q]:
                    print 'Wrong Guess Try again'
                    global f
                    f += 1
                
                else:
                    global t
                    t += 1
                    #a[p] = secretWord[p]
                    print 'Found ' + q
                    getGuessedWord(secretWord, lettersGuessed)
                    break
        if t == len(secretWord):
            
            #print a
            return True
        else:
            return False
        
    else:
        return False
'''
    


'''
def getGuessedWord(secretWord, lettersGuessed):

    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.

    # FILL IN YOUR CODE HERE...

    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise

    # FILL IN YOUR CODE HERE...
    #a = []
    #t = 0
    #f = 0
    #u = '_'
    for x in range(0,len(secretWord)):
        a.append(u)
    if len(lettersGuessed) > 0:
        for p in range (0,len(secretWord)):
            #print 'Comparing ' + secretWord[p] + ' now'
            for q in range(0,len(lettersGuessed)):
                #print 'comparing with ' + lettersGuessed[q]
                #print secretWord[p]
                #print lettersGuessed[q]
                if secretWord[p] != lettersGuessed[q]:
                    global f
                    f += 1
                else:
                    global t
                    t += 1
                    #a[p] = secretWord[p]
                    #print 'Found ' + lettersGuessed[q]
                    #print a
                    break
        if t == len(secretWord):
            d = ' '.join(a)
            getAvailableLetters(lettersGuessed)
            return d
        else:            
            d = ' '.join(a)
            getAvailableLetters(lettersGuessed)
            return d
        
    else:
        d = ' '.join(a)
        getAvailableLetters(lettersGuessed)
        return d

'''

'''
def getAvailableLetters(lettersGuessed):
    
    #lettersGuessed: list, what letters have been guessed so far
    #returns: string, comprised of letters that represents what letters have not
    #  yet been guessed.
    
    # FILL IN YOUR CODE HERE...

    
    
    if len(lettersGuessed) > 0:

            for q in range(0,len(lettersGuessed)):
                #print 'comparing with ' + lettersGuessed[q]
                #print secretWord[p]
                #print lettersGuessed[q]
                for g in l:
                    if g == lettersGuessed[q]:
                        l.remove(lettersGuessed[q])

            e = ''.join(l)
            return e

    else:
        #d = ' '.join(a)
        e = ''.join(l)    
        return e

    
'''

#def game(secretWord,lettersGuessed):




def hangman(secretWord):
    d = ''
    e = ''
    t = 0
    f = 0
    n = 8
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is" +str(len(secretWord)) + " letters long "
    print secretWord
    for x in range(0,len(secretWord)):
            a.append('_')
            #print a
    for k in range(0,n):
        print "You have " + str(n) + " guesses left"
        n -= 1
        e = ''.join(l)
        print "Available Letters: " + e
        letter = raw_input("Please guess a letter: ")
        lettersGuessed.append(letter)
        #global v
        #v = letter
        #print 'you have entered ' + letter
        #game(secretWord, lettersGuessed)
        #getAvailableLetters(lettersGuessed)
        #getGuessedWord(secretWord, lettersGuessed)



# GAME CODE FROM NOW

        #a = []
        
        
        
        #p = 0
        #q = 0
        
        
        if len(lettersGuessed) > 0:
            #for q in range (0,len(lettersGuessed)):
            #    print 'Comparing ' + lettersGuessed[q] + ' now'
                for p in range(0,len(secretWord)):
                    #print letter
                    #print 'comparing with ' + secretWord[p]
                    #print secretWord[p]
                    #print lettersGuessed[q]
                    #l.remove(letter)
                    for g in l:
                        #print l[g]
                        if g == letter:
                            #print 'abd'
                            l.remove(g)
                        
                    if secretWord[p] != letter:
                        # global f
                        f += 1
                        #print "Try Different word!!"    
                        
                    
                    else:
                        #global t
                        t += 1
                        #print "True !!"
                        #print t
                        a[p] = secretWord[p]
                        d = ' '.join(a)
                        print d
                        #print a
                        #print 'Found ' + secretWord[p]
                        #print a
                        #print 'a in loop is: ' + str(a)
                        #global p
                        #p += 1
                        #break
                            
                #global q
                #q += 1            
                #break
                if t == len(secretWord):
                    d = ' '.join(a)
                    e = ''.join(l)
                    #print 'a out of loop is: ' + str(a)
                    #print 'e out of loop is: ' + str(e)
                    #print 'd out of loop is: ' + str(d)
                    #print lettersGuessed
                    print d
                    print e
                    if d == secretWord:
                        #print "First Hurray!!"
                        return True
                    else:
                        #print "First Sorry! You Lose!!"
                        return False
                    
                    #return True
                
        else:
                d = ' '.join(a)
                e = ''.join(l)
                #print 'e is: ' + str(e)
                #print 'd is: ' + str(d)
                #print 'a is: ' + str(a)
                #print "Second Sorry! You Lose!!"
                return False



    #print "Finally d is: " + d
    if d == secretWord:
        #print "Final Hurray!!"
        return True
    else:
        print "Final Sorry! You lose!!"
        return False







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
