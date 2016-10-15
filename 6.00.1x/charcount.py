def inpchk():
    s = 'aaaaabbbbbbbbbccccpqrstuv'
    orig = 'abcdefghijklmnopqrstuvwxyz'
    list1 = []
    slist = list(s)
    n = ''
    i = 0
    '''
    while i <= len(orig):
        count = 0
        j = 0
        while orig[i] == s[j]:
            print orig[i]
            print s[j]
            count +=1
            j +=1
            l.append(orig[i])
            l.append(count)
            i += 1
            
    print l
        
    '''
    
    #print slist
    for i in orig:
        count = 0
        while i in slist:
            count += 1
            slist.remove(i)
            
        
        if count > 1:
            list1.append(i)
            list1.append(count)
        elif count == 1:
            list1.append(i)
                
    #print list1
    str1 = ''.join(map(str, list1))
    print str1
    #print ' '.join(l)
    #print p
    '''
    while i < len(slist):
        if n != slist[i]:
            
            count = slist.count(slist[i])
            n = slist[i]
            #print count
            if count > 1:
                list1.append(slist[i])
                list1.append(count)
            elif count == 1:
                list1.append(slist[i])
            i +=1
        else:
            i+=1
    str1 = ''.join(map(str, list1))
    print str1
    '''
   
            
