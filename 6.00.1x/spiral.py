i = 0
string = "abcdefghijklmnopqrstuvwxy"
list1 = []
length = len(string)
n = 5
for i in range(i,n,1):
    print i
    list1.append(string[i])
    print string[i]
i += 5
print i
for i in range(i,n-1,n):
    print i
    list1.append(string[i])
    print string[i]
i -= 1
for i in range(i,n-1,-1):
    print i
    list1.append(string[i])
    print string[i]
i -= n
for i in range(i,n-2,-n):
    print i
    list1.append(string[i])
    print string[i]
i += 1
for i in range(i,n-2,1):
    print i
    list1.append(string[i])
    print string[i]
i += n
for i in range(i,n-3,n):
    print i
    list1.append(string[i])
    print string[i]
i -= 1
for i in range(i,n-3,n):
    print i
    list1.append(string[i])
    print string[i]

print list1

    
    
