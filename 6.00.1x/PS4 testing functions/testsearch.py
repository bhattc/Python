import re
word = 'AHEAD'
def isWordValid(word):
    fil = file('words.txt')
    print word
    #if word == 'AHEAD':
    #    print 'Found word'
    #else:
    #    print 'Not found'
    for line in fil:
        print line
        if word is line:
            print "Word Found"
        else:
            print word
            print "Not a word listed"
    #if word in open('words.txt').read():
     #   print "true"
    #else:
     #   print "false"

#wordList = loadWords()
isWordValid(word)

        
    
'''
def check_string():
    #no need to pass arguments to function if you're not using them
    w = raw_input("Input the English word: ")

    #open the file using `with` context manager, it'll automatically close the file for you
    with open("words.txt") as f:
        found = False
        for line in f:  #iterate over the file one line at a time(memory efficient)
            if re.search("\b{0}\b".format(w),line):    #if string found is in current line then print it
                print line
                found = True
            if not found:
                print line
                print('The translation cannot be found!')

#check_string()
'''
