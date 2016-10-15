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
t = 0
f = None
u = '_'
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


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
    print "  ", len(wordlist), "words loade d."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def game(secretWord,lettersGuessed):
     for x in range(0,len(secretWord)):
        a.append(u)
        if len(lettersGuessed) > 0:
            for p in range (0,len(secretWord)):
                print 'Comparing ' + secretWord[p] + ' now'
                for q in range(0,len(lettersGuessed)):
                    print 'comparing with ' + lettersGuessed[q]
                    print secretWord[p]
                    print lettersGuessed[q]
                    for g in l:
                        if g == lettersGuessed[q]:
                            l.remove(lettersGuessed[q])
                    if secretWord[p] != lettersGuessed[q]:
                        global f
                        f += 1
                    
                
                    else:
                        global t
                        t += 1
                        a[p] = secretWord[p]
                    
                        #print 'Found ' + lettersGuessed[q]
                        #print a
                        #break
                if t == len(secretWord):
                    d = ' '.join(a)
                    e = ''.join(l)
            
                    print e
                    print d
                    return True
                else:
            
                    d = ' '.join(a)
                    e = ''.join(l)
                    print e
                    print d
                    return false
        
            else:
                d = ' '.join(a)
                e = ''.join(l)
                print e
                print d
                return False

def hangman(secrwtWord):
    print 'START'
    print "Word contains " + str(len(secretWord)) + " letters. "
    for k in range(0,len(secretWord)):
    
            letter = raw_input("Enter a single Letter: ")
            lettersGuessed.append(letter)
            print 'you have entered L ' + letter
            game(secretWord,lettersGuessed)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)


