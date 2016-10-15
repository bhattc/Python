total = 0
s = raw_input('enter a string')
for i in range (1,len(s)-1):
    if s[i-1 : i+2] == 'bob':
        total += 1
print total
