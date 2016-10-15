s = raw_input('enter a string :')
v = 0
w = 0
for i in range(0,len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == "o" or s[i] == "u":
        v = v + 1
        print "vowel found"
    else:
        print "not vowel"
        w = w + 1
print v
print w
