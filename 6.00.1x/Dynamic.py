
def setList(i,n, Chocolates):
    if (n>1):
        while (n >=1):
            print str(n) + "set list of n"
            Chocolates.append(n+1);
            n = n-1;
    else:
        print Chocolate[1];
        #if (Chocolates[i-1] == 1):
        #Chocolates.append(Chocolates[i-1]+1);
        #else:
        Chocolates.append(1);
            
            
def Dynamic():
    list1 = [2,4,2,6,1,7,8,9,2,1];
    #list1 = [1,2,9,8,7,1,6,2,4,2];
    Chocolate = [];
    
    '''
    for i in range(0,len(list1)):
        n=0;
        print len(list1)
        while(i < len(list1) & list1[i+1] < list1[i]):
            
            print "in while";
            n=n+1;
            if(i < len(list1)-1):
                i = i+1;
                print "value of i: " + str(i);
            print n;
            print list1[i];
        #print i;

    '''
    #list1 = [9,8,7,8];
    i = 0;
    print len(list1);
    while (i < len(list1)):
        
        n = 0;
        print list1[i];
        print "Main While";
        if (i+1 <= len(list1)-2):
            
            while (list1[i] > list1[i+1]):
                print list1[i] > list1[i+1];
                #print list1[i];
                #print i;
                if (i < len(list1)-2):
                    i = i+1;
                else:
                    print i;
                    if (i == len(list1)-2):
                        if (list1[i] > list1[i+1]):
                            n = n+1;
                            
                        print "Last Element";
                    break;
                print "less";
                n = n+1;
                #i = i+n;
                print list1[i]
        print str(i) + ": i";
        print str(n) + ": n";
        if (n>=1):
            while (n >=1):
                print str(n) + "set list of n"
                Chocolate.append(n+1);
                n = n-1;
        else:
            if (len(Chocolate) == 0 & n == 0):
                Chocolate.append(1);
            elif (list1[i-1] < list1[i]):
                Chocolate.append(Chocolate[len(Chocolate)-1]+1);
            else:
                Chocolate.append(1);
        #setList(i,n, Chocolate);
        i = i+1;
        print Chocolate;
    print "OUT OF WHILE";



        

Dynamic();
