import time
def stringdup(st):
    start = time.clock()
    a = [];
    for i in st:
        print i
        if i not in a:
            if (i == ' '):
                print i
                
            else:
                a.append(i)
            
    print a
    print time.clock()-start


def anag(st1,st2):
    x = list(st1)
    #print x
    for i in st2:
        #print i
        if i in x:
            x.remove(i)
            #print x

    if len(x) == 0:
        print "x is anagram"
    else:
        print "x is not anagram"

def check(end):
    i = 0
    j = 0
    while(i<=end):
        j = i + j
        i += 1
    print j
    
def ch():
    myStr = '6.00x'

    for char in myStr:
        print char

    print 'done' 
def che():
    greeting = 'Hello!'
    count = 0

    for letter in greeting:
        count += 1
        if count % 2 == 0:
            print letter 
        print letter

    print 'done'
def chi():
    school = 'Massachusetts Institute of Technology'
    numVowels = 0
    numCons = 0

    for char in school:
        if char == 'a' or char == 'e' or char == 'i' \
            or char == 'o' or char == 'u':
            numVowels += 1
        elif char == 'o' or char == 'M':
            print char
        else:
            numCons -= 1

    print 'numVowels is: ' + str(numVowels)
    print 'numCons is: ' + str(numCons) 

def numcheck():
    num = 10
    for num in range(5):
        print num
    print num

def numcheck1():
    divisor = 2
    for num in range(0, 10, 2):
        print num/divisor 

def numcheck2():
    for variable in range(20):
        if variable % 4 == 0:
            print variable
        if variable % 16 == 0:
            print 'Foo!' 
def c():
    for letter in 'hola':
        print letter

def c1():
    count = 0
    for letter in 'Snow!':
        print 'Letter # ' + str(count) + ' is ' + str(letter)
        count += 1
        break
    print count
