s1 = 'abcdHJSDHFKJSHDFK'
s2 = 'efghi'

if len(s1) > len(s2):
    (s1, remainder) = (s1[0:len(s2)], s1[len(s2):])
    #print remainder
elif len(s1) < len(s2):
    
    (s2, remainder) = (s2[0:len(s1)], s2[len(s1):])
    #print remainder
else:
    remainder = ""

char = []
for i in range(len(s1)):
    char.append(s1[i])
    char.append(s2[i])

result = "".join(char) + remainder
print result
