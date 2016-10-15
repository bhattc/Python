def SplitArray():
    #P = [1,2,3,4,5,-6,7,8,9,10,200,-1000,100,250,-720,1080,200,300,400,500,50,74];
    P = [150,30,450,60];
    #Q = abs(P);
    #print Q;
    sum (P)
    L = [];
    R = [];

    for i in P:
        if(sum(L) == sum(R)):
            L.append(i);
        elif (sum(L) < sum(R)):
            L.append(i);
        elif (sum(L) > sum(R)):
            R.append(i);
    print(str(L) + ' : '+str(sum(L)));
    print(str(R) + ' : '+ str(sum(R)));

SplitArray();
    

    
