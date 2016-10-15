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
a = []
d = ''
t = 0
f = 0
u = '_'
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
p = 0
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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    #a = []

    #u = '_'
    #for x in range(0,len(secretWord)):
     #   a.append(u)
            #for q in lettersGuessed:
            #print 'Comparing ' + p + ' now'
    for p in range(len(secretWord)):
                #print 'comparing with ' + lettersGuessed[q]
                #print secretWord[p]
                #print lettersGuessed[q]
        if secretWord[p] != lettersGuessed[-1]:
            global f
            f += 1
                
        else:
            global t
            t += 1
            #a[p] = secretWord[p]
            print 'Found ' + secretWord[p]
            getGuessedWord(secretWord, lettersGuessed)
            #break

        #if t == len(secretWord):
        #    #print a
        #    return True
        #else:
        #    return False



    



def getGuessedWord(secretWord,lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise

    # FILL IN YOUR CODE HERE...
    #a = []
    #t = 0
    #f = 0
    #u = '_'

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
                    '''
    print a
    print p
    a[p] = secretWord[p]
    d = ' '.join(a)
    print d
    if d == secretWord:
        print "YES We Found it ! !"
    else:
        print "Sorry You Lose!"
    #getAvailableLetters(lettersGuessed)
                    #print 'Found ' + lettersGuessed[q]
                    #print a
'''
                    break
        if t == len(secretWord):
            d = ' '.join(a)
            return d
        else:            
            d = ' '.join(a)
            return d
        
    else:
        d = ' '.join(a)
        return d

'''


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    
    
    for g in l:
        if g == secretWord[p]:
            l.remove(g)

            e = ''.join(l)
            print e
        else:
            e = ''.join(l)

            print e


    

def hangman(secretWord):
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
    print "START"
    print "Word contains " + str(len(secretWord)) + "letters. "
    getAvailableLetters(lettersGuessed)
    print secretWord
    for x in range(0,len(secretWord)):
        a.append('_')
    for k in range(0,len(secretWord)):
    
        letter = raw_input("Enter a single Letter: ")
        lettersGuessed.append(letter)
        print 'you have entered ' + letter
        print lettersGuessed
        if len(lettersGuessed) > 0:
            isWordGuessed(secretWord, lettersGuessed)
        else:
            print "Enter atlease single letter!!"
        #getAvailableLetters(lettersGuessed)
        #getGuessedWord(secretWord, lettersGuessed)

    if d == secretWord:
        return True
    else:
        return False







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
