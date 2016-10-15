def calculateSum(str1):
    tot = 0;
    str2 = "";
    str3 = "";
    str4 = "";
    j = 0;
    for i in str1:
        if(i.isdigit()):
            if (j == 0):
                tot += int(i);
                str2 += i;
                
            else:
                if (str2 == ""):
                    str2 += i;
                else:
                    str2 += ","+i;
            j = 0;
        else:
            str3 += i;
            j = 1;
    print tot;
    print str2;
    print str3;
        
calculateSum("sanket-241-patel 32.");
