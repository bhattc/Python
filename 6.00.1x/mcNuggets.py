n = int(raw_input("enter an integer value of McNugget you want:"))
c = 0
b = 0
a = 0

def McNuggets(n):
    global a,b,c
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    #print n
    
    if n >= 20:
        c += 1
        n -= 20
        return McNuggets(n)
    elif n < 20 and n >= 9:
        b +=1
        n -= 9
        return McNuggets(n)
    elif n < 9 and n >= 6: 
        a += 1
        n -= 6
        return McNuggets(n)
    else:
        if n == 0:
            print True
            print a,b,c
        else:
            print False
            print a,b,c
    
McNuggets(n)        
