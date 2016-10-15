
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

word = 'poet'
n = 5

def getWordScore(word, n):
    total = 0
        #for line in words.txt:
        #    if word in line:
         #       print "Word Found"
            
    l = list(word)
        #print l
    for w in l:
        #   print w
            #print SCRABBLE_LETTER_VALUES[w]
        total += SCRABBLE_LETTER_VALUES.get(w,0)
    total = total * len(l)
    if len(l) == n:
        total += 50
        return total
    else:
        return total
